 
import bpy
from var import except_msg
from utils import (active_object, 
                    select_all,
                    mode_set,
                    sorting_objects, 
                    armature_name, 
                    figure_name, 
                    accessories, 
                    SUCCESS, 
                    INPUT_ERR,
                    ERROR, 
                    purge_scene, 
                    empty_name_holders,
                    sorting_armature,
                    copy_mixam_transform
)

def del_object(obj):
    select_all('DESELECT')
    active_object(obj)
    objs = bpy.data.objects
    if figure_name:
        objs[figure_name[0]].select_set(True)
    elif accessories:
        for a in accessories:
            objs[a].select_set(True)
    bpy.ops.object.delete()
    purge_scene()

def remove_CT_constraints():
    obj = bpy.context.object
    mode_set('POSE')
    for bone in obj.pose.bones:
        CT = [c for c in bone.constraints
        if c.type == 'COPY_TRANSFORMS'
        or c.type == 'COPY_ROTATION']
        for c in CT:
            bone.constraints.remove(c)

def adjust_framelength():
    obj = bpy.context.object
    action = obj.animation_data.action
    fcurve =  action.fcurves[0]
    keyframes = list(fcurve.keyframe_points)
    frames = len(keyframes)
    bpy.context.scene.frame_end = frames

def disable_GNSrig():
    mode_set('OBJECT')
    select_all('DESELECT')
    objs = bpy.data.objects
    rig_coll = objs['rig'].users_collection[0]
    widgt_coll = bpy.data.collections['Widgets']
    widgt_coll.objects.link(objs['GNSrig'])
    rig_coll.objects.unlink(objs['GNSrig'])
    for meshes in objs:
        if meshes.modifiers:
            for mod in meshes.modifiers:
                if (mod.type == "ARMATURE" 
                and mod.object.name == "GNSrig"):
                    mod.show_viewport = False
                    
    active_object('rig')

def enable_GNSrig():
    objs = bpy.data.objects
    rig_collection = objs['rig'].users_collection
    GNS_collection = objs['GNSrig'].users_collection
    rig_collection[0].objects.link(objs['GNSrig'])
    GNS_collection[0].objects.unlink(objs['GNSrig'])

    for meshes in objs:
        if meshes.modifiers:
            for mod in meshes.modifiers:
                if (mod.type == "ARMATURE" 
                and mod.object.name == "GNSrig"):
                    mod.show_viewport = True
                    
    mode_set('OBJECT')
    select_all('DESELECT')
    active_object('GNSrig')
    bpy.context.object.animation_data_create()
    
    
def tilt_mixamo_bones(val, index1, index2):
    if not armature_name:
        sorting_armature()
    objs = bpy.data.objects
    action = objs[armature_name[0]].animation_data.action
    fcurve =  list(action.fcurves)
    for fc in fcurve:
        keyframes = list(fc.keyframe_points)   
    framelength = len(keyframes)
    for fr in range(framelength):
        y1 = action.fcurves[index1].keyframe_points[fr].co[1]
        action.fcurves[index1].keyframe_points[fr].co[1] = y1 + val
        y2 = action.fcurves[index2].keyframe_points[fr].co[1]
        action.fcurves[index2].keyframe_points[fr].co[1] = y2 + val

def bake_mixamo():
    empty_name_holders()
    sorting_armature()
    mode_set('OBJECT')
    objs = bpy.data.objects
    obj = bpy.context.object
    obj.animation_data_clear()
    Arma_coll = objs[armature_name[0]].users_collection[0]
    Arma_coll.hide_viewport = False
    x = bpy.context.scene.frame_start
    y = bpy.context.scene.frame_end
    bpy.ops.nla.bake(frame_start=x, frame_end=y, \
        only_selected=False, visual_keying=True, \
        clear_constraints=True, bake_types={'POSE'})
    for animdata in bpy.data.actions:
        animdata.use_fake_user = True
    Arma_coll.hide_viewport = True
    mixamo_remove()
    enable_GNSrig() 
                        
def mixamo_copy():
    mode_set('OBJECT')
    empty_name_holders()
    sorting_armature()
    objs = bpy.data.objects
    b=[]
    for a in objs:
        if a.type == 'ARMATURE':
            if a.name[:8] == "Armature" or a.name[:7] == 'Genesis':
                b.append(a)
                
    Arma2 = [ob for ob in bpy.data.objects 
            if ob.name == 'GNSrig']
    if not Arma2:
        return [ERROR, except_msg[10]]
    Arma = [arm for arm in objs
        if arm.type == 'ARMATURE' 
        and (arm.name[:8] == 'Armature' 
        or arm.name[:7] == 'Genesis')]
    if not Arma:
        return [ERROR, except_msg[11]]
    
    try:
        posebones = Arma2[0].pose.bones
        const = posebones['hip'].constraints['Copy Transforms']
        if const:
            if  len(b) > 1:
                for bone in Arma2[0].pose.bones:
                    CT = [c for c in bone.constraints
                    if c.type == 'COPY_TRANSFORMS'
                    or c.type == 'COPY_ROTATION']
                    for c in CT:
                        bone.constraints.remove(c)
                                  
                for a in b:
                    if a.users_collection[0].name == "Widgets":
                        b.remove(a)
                        a.users_collection[0].objects.unlink(a)
                        purge_scene()
                        
            else:
                return [ERROR, except_msg[12]]
    except:
        pass
                
    for a in b:
        if a.users_collection[0].name == "Widgets":
            b.remove(a)
            a.users_collection[0].objects.unlink(a)
            purge_scene()
            
    if  len(b) > 1:
        b.clear()
        return [ERROR, except_msg[12]]
    else:
        empty_name_holders()
        sorting_armature()
        if Arma2[0].users_collection[0].hide_viewport == False:
            disable_GNSrig()
        rig_coll = objs['rig'].users_collection[0]
        GNS_coll = objs['GNSrig'].users_collection[0]
        if GNS_coll != rig_coll:
            GNS_coll.hide_viewport = False
        select_all('DESELECT')
        active_object('GNSrig')
        obj = bpy.context.object
        obj.data.display_type = 'STICK'    
        copy_mixam_transform()
        mode_set('OBJECT')
        obj.animation_data_clear()
        select_all('DESELECT')
        arma3 = armature_name[0]
        active_object(arma3)     
        obj = bpy.context.object
        armature_coll = obj.users_collection
        for chd in bpy.context.object.children:
            chd.select_set(True)
        obj.select_set(False)
        bpy.ops.object.delete()
        active_object(armature_name[0])
        widget_coll = bpy.data.collections['Widgets']
        widget_coll.objects.link(obj)
        armature_coll[0].objects.unlink(obj)
        select_all('DESELECT')
        adjust_framelength()
        enable_GNSrig()
        empty_name_holders()
        sorting_objects()
        active_object('GNSrig')
        if figure_name[0][:8] == 'Genesis8':
            if arma3[:8] == 'Armature':
                tilt_mixamo_bones(-0.4, 266, 76)
                tilt_mixamo_bones(0.05, 446, 446)
                tilt_mixamo_bones(-0.05, 486, 486)
            elif arma3[:8] == 'Genesis3':
                tilt_mixamo_bones(-0.4, 666, 416)
                tilt_mixamo_bones(-0.05, 196, 196)
                tilt_mixamo_bones(0.05, 26, 26)
            elif arma3[:8] == 'Genesis2':
                tilt_mixamo_bones(-0.4,  376, 586)
                tilt_mixamo_bones(-0.05, 116, 116)
                tilt_mixamo_bones(0.05, 26, 26)
        if GNS_coll != rig_coll:
            GNS_coll.hide_viewport = True
        return [SUCCESS]
    
def mixamo_remove():
    empty_name_holders()
    sorting_armature()
    mode_set('OBJECT')
    objs = bpy.data.objects
    rig_coll = objs['rig'].users_collection[0]
    Arma_coll = objs[armature_name[0]].users_collection[0]
    GNS_coll = objs['GNSrig'].users_collection[0]
    for animdata in bpy.data.actions:
        if (animdata.name[:8] == 'Armature' 
        or animdata.name[:7] == 'Genesis'):
            animdata.use_fake_user = False
            animdata.user_clear()
            
    purge_scene()
    if Arma_coll != rig_coll:
        if GNS_coll != rig_coll:
            enable_GNSrig()
        try:
            posebones = objs['GNSrig'].pose.bones
            if posebones['hip'].constraints['Copy Transforms']:
                remove_CT_constraints()
        except:
            pass
        disable_GNSrig()
        widget_coll = bpy.data.collections['Widgets']
        widget_coll.hide_viewport = False
        del_object(armature_name[0])
        active_object('rig')
        widget_coll.hide_viewport = True
    else:
        del_object(armature_name[0])
        active_object('rig')
        
