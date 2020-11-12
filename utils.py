import bpy
from mathutils import Matrix
from math import radians

from materials import adjust_materials
from var import (
                arm1_bonepole_verts, 
                arm2_bonepole_verts, 
                bones_influence,
                fingerbones, 
                face_controls, 
                toebones, 
                facialbones,
                facialbones2, 
                FaceHeadParent, 
                eyebones, 
                browbones, 
                adjust_bones,
                spine_target,
                deform_bones,
                hand_bones,
                bones_target_bones, 
                arm2_bones_target, 
                rename_rig, 
                custom_objs,
                mixamo_bones,
                except_msg,
                fcurves_indexes,
                except_msg
                )                
                 
armature_name = []
figure_name = []
accessories = []
matrix = []

INPUT_ERR = 'ERROR_INVALID_CONTEXT'
ERROR = 'ERROR'
WARNING = "WARNING"
SUCCESS = "OK"

def mode_set(set_mode):
    bpy.ops.object.mode_set(mode=set_mode)

def select_all(cmd):
    if bpy.context.mode == 'OBJECT':
        bpy.ops.object.select_all(action=cmd)
    elif bpy.context.mode == 'EDIT_MESH':
        bpy.ops.mesh.select_all(action=cmd)
    elif bpy.context.mode == 'EDIT_ARMATURE':
        bpy.ops.armature.select_all(action=cmd)
    elif bpy.context.mode == 'POSE':
        bpy.ops.pose.select_all(action=cmd)

def active_object(obj):
    view_layer = bpy.context.view_layer
    objs = bpy.data.objects
    view_layer.objects.active = objs[obj]
    objs[obj].select_set(True)

def sorting_objects():
    objs = bpy.data.objects
    for obj in objs:
        if (obj.type == 'ARMATURE' 
        and obj.name[:7] == 'Genesis' 
        and len(obj.data.bones) > 160):
            armature_name.append(obj.name)
        elif obj.type == "MESH":
            if obj.name[:7] == 'Genesis':
                figure_name.append(obj.name)
                if (obj.parent.name == 'rig' 
                or obj.parent.name == 'GNSrig'):
                    figure_name.clear()
                    figure_name.append(obj.name)
    for obj in objs:
        if obj.parent and obj.type == "MESH":
            if (len(obj.data.vertices) > 500 
            and obj.parent.name == 
            objs[figure_name[0]].parent.name):
                accessories.append(obj.name)

def sorting_armature():
    for ob in bpy.data.objects:
        if ob.type == 'ARMATURE':
            if (ob.name != 'rig' 
            and ob.name != 'GNSrig'):
                armature_name.append(ob.name)
                for chld in ob.children:
                    accessories.append(chld.name)
                    if chld.name[:7] == 'Genesis':
                        accessories.remove(chld.name)
                        figure_name.append(chld.name)    
            
def join_mini_accessories():
    objs = bpy.data.objects
    for msh in bpy.data.objects:
        if (msh.type == 'MESH' 
        and len(msh.data.vertices) < 500):
            objs[msh.name].select_set(True)
            if figure_name:
                active_object(figure_name[0])
                bpy.ops.object.join()
            
def rename_arma_figure():
    mode_set('OBJECT')
    active_object(armature_name[0])
    mode_set('EDIT')
    for bone in bpy.context.object.pose.bones:
        if (bone.name[0] == 'l' 
        and bone.name != "lowerFaceRig" 
        and bone.name != "lowerJaw" 
        and bone.name != "lowerTeeth"):
            newname=bone.name[1:] + '.L'
            bone.name=newname
        elif bone.name[0] == 'r':
            newname=bone.name[1:] + '.R'
            bone.name=newname
    
def scale_bones(armature, bone, val):
    matrix = []
    objs = bpy.data.objects
    select_all('DESELECT')
    arma = objs[armature]
    editbones = arma.data.edit_bones
    editbones[bone].select = True
    mode_set('OBJECT') 
    mode_set('EDIT')
    matrix.append(editbones[bone].matrix)
    bpy.ops.transform.resize(value=(val, val, val))
    editbones[bone].matrix = matrix[0]
    matrix.clear()
    select_all('DESELECT')
    
def match_bone_mesh(armature, mylist):
    objs = bpy.data.objects
    obj = objs[figure_name[0]]
    vertices = obj.data.vertices
    editbones = armature.data.edit_bones
    for fill in mylist:
        bone, head_tail = fill[0], fill[1]
        if armature_name[0] == 'Genesis3Male':
            vn = fill[2]
        elif armature_name[0] == 'Genesis3Female':
            vn = fill[3]
        elif armature_name[0] == 'Genesis8Female':
            vn = fill[4]
        elif armature_name[0] == 'Genesis8Male':
            vn = fill[5]
        if len(fill) == 6:
            if head_tail == 'head':
                editbones[bone].head.xyz = vertices[vn].co.xyz
            else:
                editbones[bone].tail.xyz = vertices[vn].co.xyz
        else:
            if fill[-1] == 'y':
                if head_tail == 'head':
                    editbones[bone].head.y = vertices[vn].co.y
                else:
                    editbones[bone].tail.y = vertices[vn].co.y
            if fill[-1] == 'yz':
                if head_tail == 'head':
                    editbones[bone].head.yz = vertices[vn].co.yz
                else:
                    editbones[bone].tail.yz = vertices[vn].co.yz
            elif fill[-1] == 'xz':
                editbones[bone].tail.xz = vertices[vn].co.xz
            elif fill[-1] == 'xy':
                editbones[bone].tail.xy = vertices[vn].co.xy
            elif fill[-1] == 'z':
                editbones[bone].head.z = vertices[vn].co.z
           
def match_bone_armature(mylist, armature1, armature2):
    editbones1 = armature1.data.edit_bones
    editbones2 = armature2.data.edit_bones
    for fill in mylist:
        bone1, head_tail = fill[0], fill[1]
        bone2, tail_head = fill[2], fill[3]
        if head_tail == 'head' and tail_head == 'head':
            editbones1[bone1].head.xyz = editbones2[bone2].head.xyz
        elif head_tail == 'head' and tail_head == 'tail':
            editbones1[bone1].head.xyz = editbones2[bone2].tail.xyz
        elif head_tail == 'tail' and tail_head == 'tail':
            editbones1[bone1].tail.xyz = editbones2[bone2].tail.xyz
        else:
            editbones1[bone1].tail.xyz = editbones2[bone2].head.xyz              

def constraints_influence(mylist):
    posebones = bpy.context.object.pose.bones
    for fill in mylist:
        bone = fill[0]
        const = fill[1]
        value = fill[2]
        posebones[bone].constraints[const].influence = value
        
def bone_constraint(arm, bn, ctype, cnst, strgt, tspc=None):
    global posebones
    objs = bpy.data.objects
    posebones = bpy.context.object.pose.bones 
    posebones[bn].constraints.new(type= ctype)
    posebones[bn].constraints[cnst].target = objs[arm]
    posebones[bn].constraints[cnst].subtarget = strgt
    if tspc:
        posebones[bn].constraints[cnst].target_space = tspc
        posebones[bn].constraints[cnst].owner_space = tspc
            
def empty_name_holders():     
    if armature_name:
        armature_name.clear()
    if figure_name:
        figure_name.clear()
    if accessories:
        accessories.clear()
        
def bone_zrotation(bon, val):
    bone = bpy.context.object.data.edit_bones[bon]
    x, y, z = bone.matrix.to_3x3().col
    R = (Matrix.Translation(bone.head) @ 
            Matrix.Rotation(radians(val), 4, z) @
            Matrix.Translation(-bone.head))
    bone.transform(R)
    
def bone_xrotation(bon, val):
    bone = bpy.context.object.data.edit_bones[bon]
    x, y, z = bone.matrix.to_3x3().col
    R = (Matrix.Translation(bone.head) @ 
            Matrix.Rotation(radians(val), 4, x) @
            Matrix.Translation(-bone.head))
    bone.transform(R)

def select_material_slot(mat_name):
    a = list(bpy.context.object.data.materials)
    b = a.index(bpy.data.materials[mat_name])
    bpy.context.object.active_material_index = b
    bpy.ops.object.material_slot_select()

def purge_scene():
    for blocks in bpy.data.armatures:
        if blocks.users == 0:
            bpy.data.armatures.remove(blocks)
    for blocks in bpy.data.objects:
        if blocks.users == 0:
            bpy.data.objects.remove(blocks)
    for blocks in bpy.data.meshes:
        if blocks.users == 0:
            bpy.data.meshes.remove(blocks)
    for blocks in bpy.data.materials:
        if blocks.users == 0:
            bpy.data.materials.remove(blocks)
    for blocks in bpy.data.images:
        if blocks.users == 0:
            bpy.data.images.remove(blocks)
    for blocks in bpy.data.actions:
        if blocks.users == 0:
            bpy.data.actions.remove(blocks)
    
def make_custom_object(bone, widget,scale):
    obj = bpy.context.object
    objs = bpy.data.objects
    obj.pose.bones[bone].custom_shape = objs[widget]
    obj.pose.bones[bone].custom_shape_scale = scale
    

def copy_mixam_transform():
    a=[]
    obj  = bpy.context.object
    posebones = obj.pose.bones
    for fill in mixamo_bones:
        bone, target = fill[0], fill[1]
        if len(fill) > 3:
            x = (bone, 'mixamorig:'+target)
            a.append(x)
        else:
            x = (bone + '.R', 'mixamorig:Right'+ target)
            a.append(x)
            x = (bone + '.L', 'mixamorig:Left'+ target)
            a.append(x)
            
    for fill in a:
        source, target = fill[0], fill[1]
        for pb in posebones:
            if pb.name == source:
                if pb.name == 'hip':
                    bone_constraint(armature_name[0], pb.name, 
                    'COPY_TRANSFORMS', "Copy Transforms", target)
                else:
                    bone_constraint(armature_name[0], pb.name, 
                    'COPY_ROTATION', "Copy Rotation", target, tspc='LOCAL')
    a.clear()
    if armature_name[0][:8] == 'Genesis8':
        for bone in hand_bones:
            if (bone not in adjust_bones 
            and bone[:7] != 'Forearm'):
                CR = [c for c in posebones[bone].constraints
                if c.type == 'COPY_ROTATION']
                for c in CR:
                    posebones[bone].constraints["Copy Rotation"].invert_x = True
                    posebones[bone].constraints["Copy Rotation"].invert_y = True
                    posebones[bone].constraints["Copy Rotation"].invert_z = True

   
def convert_to_mixamo():
    empty_name_holders()
    sorting_armature()
    objs = bpy.data.objects
    b=[]
    for a in bpy.data.objects:
        if a.type == 'ARMATURE':
            if( a.name[:8] == "Armature" 
            or a.name[:7] == 'Genesis'
            or a.name[:5] == 'Donor'):
                b.append(a)
    
    if (armature_name[0][:7] == 'Genesis'
    and objs[armature_name[0]].children):
        pass
    elif armature_name[0][:5] == 'Donor':
        donor = armature_name[0]
        a = objs[donor].name = objs[donor].name[6:]
        armature_name.clear()
        armature_name.append(a)
    else:
        for a in b:
            if a.children or a.name[:5] == 'Donor':
                if a.name[:5] == 'Donor':
                    a.name = a.name[6:]
                armature_name.clear()
                armature_name.append(a.name)
                
    Arma2 = [ob for ob in objs 
    if ob.name == 'GNSrig']
    if not Arma2:
        return [ERROR, "Cannot execute: \n \
        Please complete rigging process and try again"]
    else:
        pass
    prepare_armature()
    if accessories:
        for slt in accessories:
            objs[slt].select_set(True)
            
    bpy.ops.object.delete()
    active_object(armature_name[0])
    mode_set('EDIT')
    select_all('SELECT')
    mode_set('POSE')
    area = bpy.context.area
    old_type = area.type
    area.type = 'DOPESHEET_EDITOR'
    bpy.ops.action.select_all(action='SELECT')
    bpy.ops.action.keyframe_type(type='KEYFRAME')
    bpy.ops.transform.transform(mode='TIME_SCALE',
                                value=(1, 0, 0, 0))
    bpy.ops.anim.channels_expand()
    bpy.ops.anim.channels_select_all(action='DESELECT')
    arma = bpy.context.object
    for i in range(9):
        arma.animation_data.action.fcurves[i].select = True
    bpy.ops.anim.channels_delete()
    area.type = old_type
    mode_set('EDIT')
    editbones = arma.data.edit_bones
    for fill in mixamo_bones:
        oldname, newname  = fill[0], fill[1]
        mxm = 'mixamorig:'
        if len(fill) == 4:
            g2n = fill[2]
            if armature_name[0][:8] == 'Genesis2':
                if (g2n == 'neck' 
                or g2n == 'chest' 
                or g2n == 'abdomen2'
                or g2n == 'abdomen'):
                    editbones[g2n].name = mxm+newname
                else:
                    editbones[oldname].name = mxm+newname
            else:
                editbones[oldname].name = mxm+newname
        elif len(fill) == 3:
            g2n = fill[2]
            if armature_name[0][:8] == 'Genesis2':
                if (g2n == 'Shldr' 
                or g2n == 'ForeArm' 
                or g2n == 'Thigh'):
                    editbones[g2n+'.R'].name = mxm+'Right'+newname
                    editbones[g2n+'.L'].name = mxm+'Left'+newname
                else:
                    editbones[oldname+'.R'].name = mxm+'Right'+newname
                    editbones[oldname+'.L'].name = mxm+'Left'+newname
            else:
                editbones[oldname+'.R'].name = mxm+'Right'+newname
                editbones[oldname+'.L'].name = mxm+'Left'+newname
    
    mode_set('OBJECT') 
    return [SUCCESS]
   
def prepare_armature():
    select_all('DESELECT') 
    join_mini_accessories()
    rename_arma_figure()
    mode_set('EDIT')
    obj = bpy.context.object
    obj.data.use_mirror_x = True
    select_all('DESELECT')
    if armature_name[0][:8] == 'Genesis8':
        for HB in hand_bones:
            if (HB != 'ThighBend.R' 
            and HB != 'ThighTwist.R' 
            and HB != 'Shin.R'):
                bone_zrotation(HB, 45)
            else:
                bone_zrotation(HB, 7)
        bone_xrotation('Shin.R', -4)
        if armature_name[0][:9] == 'Genesis8F':
            bone_xrotation('Foot.R', 180)
        else:
            bone_xrotation('Foot.R', -90)
        mode_set('OBJECT')
        active_object(figure_name[0])
        bpy.ops.object.modifier_apply(modifier=armature_name[0])
        active_object(armature_name[0])
        mode_set('POSE')
        select_all('SELECT')
        bpy.ops.pose.transforms_clear()
        bpy.ops.pose.armature_apply(selected=False)
        select_all('DESELECT')
        mode_set('EDIT')
        obj = bpy.context.object
        try:
            obj.animation_data.action
            action = obj.animation_data.action
            fcurves =  action.fcurves
            for fcI in fcurves_indexes:
                fcurves[fcI].mute = True
            
            for bone in obj.data.edit_bones:
                if bone.name[:10] == 'ShldrTwist':
                    bone.select = True
            mode_set('POSE')
            bpy.ops.pose.transforms_clear() 
            mode_set('EDIT')
            select_all('DESELECT')
            editbones = obj.data.edit_bones
            obj.data.use_mirror_x = False
            for bone in hand_bones:
                if (bone not in adjust_bones 
                and bone[:7] != 'Forearm'):
                    editbones[bone].select = True
                    bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Y')
                    select_all('DESELECT')
        except:      
            pass
                
        if armature_name[0][:9] == 'Genesis8M':
            editbones = obj.data.edit_bones
            editbones['Foot.L'].select = True
            bpy.ops.armature.calculate_roll(type='GLOBAL_NEG_Y')
            select_all('DESELECT')
            
    if armature_name[0][:8] != 'Genesis2':
        editbones = obj.data.edit_bones
        try:
            obj.animation_data.action
            pass
        except:
            match_bone_mesh(obj, arm1_bonepole_verts) 
            match_bone_armature(bones_target_bones, obj, obj)
        editbones['Eye.R'].tail.y = editbones['Eye.R'].head.y
        obj.data.use_mirror_x = False
        for bone in adjust_bones:
            editbones[bone].select = True
        bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Y')
        select_all('DESELECT')
        
        for bones in facialbones:
            if bones != 'Heel' and bones != 'Eye':
                rightbones = bones + '.R'
                scale_bones(armature_name[0], rightbones, 0.2)
                leftbones = bones + '.L'
                scale_bones(armature_name[0], leftbones, 0.2)
        for bones in facialbones2:
            scale_bones(armature_name[0], bones, 0.2)
    mode_set('OBJECT')
    obj.data.layers_protected[31] = True 
    obj.data.layers_protected[30] = True
    select_all('DESELECT')
    if figure_name:
        active_object(figure_name[0])

def initialize():
    global active_item
    viewlayer = bpy.context.view_layer
    active_item = viewlayer.objects.active
    sel_objs = bpy.context.selected_objects
    selected = list(sel_objs)
    aux_arm = []
    mode_set('OBJECT')
    arms = bpy.data.armatures
    for arm in arms:
        if (arm.users > 0 
        and arm.name[:7] == 'Genesis'): 
            aux_arm.append(arm.name)
        if (arm.users == 0 
        and arm.name[:7] == 'Genesis'):
            return [INPUT_ERR, except_msg[1]]
        if len(aux_arm) > 1:
            aux_arm.sort()
            return[INPUT_ERR, except_msg[2]
            % str.join("', '", aux_arm)] 
    objs = bpy.data.objects
    for obj in objs:
        if (obj.name[:7] == 'Genesis' 
        and obj.users > 0):
            if not selected:
                return [INPUT_ERR, except_msg[3]
                % obj.name]
            elif active_item.type != 'ARMATURE':
                return [INPUT_ERR, except_msg[4]
                % (active_item.name, active_item.type, obj.name)]
            elif active_item.name[:7] != 'Genesis':
                return [INPUT_ERR, except_msg[5]
                % (active_item.name, obj.name)]
    for obj in objs:  
        if obj.name[:7] != 'Genesis' and obj.users > 0:
            if not selected:
                return [INPUT_ERR, except_msg[6]]
            elif active_item.type != 'ARMATURE':
                return [INPUT_ERR, except_msg[7]
                % (active_item.name, active_item.type)]
            elif active_item.name[:7] != 'Genesis':
                return [INPUT_ERR, except_msg[8]
                % (active_item.name)]
    if (active_item.type == 'ARMATURE' 
    and active_item.name[:7] == 'Genesis'):   
        empty_name_holders()
        sorting_objects()
        if not figure_name:
            return [INPUT_ERR, except_msg[9]
            % armature_name[0]]
        else:
            pass
        prepare_armature()   
        if figure_name[0][:8] == 'Genesis3':
            modifier = objs[figure_name[0]].modifiers[armature_name[0]]
            objs[figure_name[0]].modifiers.remove(modifier)
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM') 
        
        if accessories:
            for slt in accessories:
                objs[slt].select_set(True)
                bpy.ops.object.make_links_data(type='MODIFIERS')
        select_all('DESELECT')
        active_object(figure_name[0])
        bpy.ops.object.transform_apply(location=True, 
                                        rotation=True, 
                                        scale=True)
        select_all('DESELECT')
        active_object(armature_name[0])
        adjust_materials()
        return[SUCCESS]

def add_metarig():
    if not armature_name:
        sorting_objects()
    scene = bpy.context.scene
    obj = bpy.context.object
    scene.cursor.location = obj.location
    bpy.ops.object.armature_human_metarig_add()
    obj = bpy.context.object
    obj.data.layers_protected[31] = True
    obj.data.layers_protected[30] = False
    obj.data.layers_protected[29] = True
 
def rig_match():
    if not armature_name:
        sorting_objects()
    objs = bpy.data.objects
    arm1 = objs[armature_name[0]]
    mode_set('EDIT')
    obj = bpy.context.object
    obj.data.use_mirror_x = True
    select_all('DESELECT')
    arm2 = objs['metarig']
    match_bone_mesh(arm2, arm2_bonepole_verts)
    editbones = obj.data.edit_bones
    for bone in editbones:
        if (bone.name[:8] == 'forehead' 
        or bone.name[:6] == 'temple'):
            editbones[bone.name].select_head = True
    multi = editbones['forehead.L'].length
    value = multi * 0.075
    bpy.ops.transform.translate(value=(0, 0, value))
    mode_set('OBJECT')  
    bpy.ops.object.transform_apply(location=True,
                                    rotation=True, 
                                    scale=True)
    select_all('DESELECT')
    active_object(armature_name[0])
    bpy.ops.object.duplicate_move() 
    coll = bpy.context.collection
    coll.objects.unlink(objs[armature_name[0] + '.001'])
    active_object(armature_name[0])
    bpy.ops.object.transform_apply(location=True, 
                                    rotation=True, 
                                    scale=True)
    active_object('metarig')
    mode_set('EDIT')
    obj = bpy.context.object
    obj.data.use_mirror_x = True
    select_all('DESELECT')
    match_bone_armature(arm2_bones_target, arm2, arm1)
    editbones1 = arm1.data.edit_bones
    editbones2 = arm2.data.edit_bones
    if armature_name[0][:8] != 'Genesis8':
        heel1 = editbones1['Heel.R']
        heel2 = editbones2['heel.02.R']
        heel1.tail.xyz = heel2.tail.xyz
        heel1.head.xyz = heel2.head.xyz
    for bone in objs['metarig'].data.edit_bones:
        if bone.name == "spine.003":
            bone.select=True
    bpy.ops.armature.subdivide(number_cuts=2)
    match_bone_armature(spine_target, arm2, arm1)
    select_all('DESELECT')
    mode_set('OBJECT')
    select_all('DESELECT')
    active_object(armature_name[0])
    bpy.ops.object.delete() 
    coll = bpy.context.collection
    coll.objects.link(objs[armature_name[0] + '.001'])
    objs[armature_name[0] + '.001'].name = armature_name[0]
    #Correcting hip orientation
    active_object(armature_name[0])
    obj = bpy.context.object
    mode_set('EDIT')
    editbones = obj.data.edit_bones
    editbones['hip'].tail[2] = editbones['hip'].head[2]
    mode_set('OBJECT')
    select_all('DESELECT')
    active_object('metarig')
    bpy.ops.object.transform_apply(location=True, 
                                    rotation=True, 
                                    scale=True)
    obj = bpy.context.object
    obj.data.layers_protected[30] = False
    obj.data.layers_protected[29] = False
    obj.data.layers_protected[28] = True
    
def generate_rig():
    try:
        if not armature_name:
            sorting_objects()
        obj = bpy.context.object
        obj.data.layers_protected[28] = False
        bpy.ops.pose.rigify_generate()
        purge_scene()
        obj = bpy.context.object
        obj.data.layers_protected[31] = True
        obj.data.layers_protected[27] = True
    except:
        pass
    
def rig_genesis_figure():
    if not armature_name:
        sorting_objects()
    obj = bpy.context.object
    obj.data.layers_protected[27] = False 
    mode_set('EDIT')
    for num in range(29, 32):
        obj.data.layers[num] = True
    for bones in face_controls:
        scale_bones('rig', bones, 0.4)             
    for bone in obj.data.edit_bones:
        if bone.name[:-2] in fingerbones:
            bone.select=True       
    bpy.ops.armature.calculate_roll(type='GLOBAL_NEG_Z')
    select_all('DESELECT')
    mode_set('OBJECT')
    active_object(figure_name[0])
    #Separating teeth 
    mode_set('EDIT')
    select_all('DESELECT')   
    for mat in bpy.context.object.data.materials:
        if mat.name[:5] == "Teeth":
            select_material_slot(mat.name)
    bpy.ops.mesh.separate(type='SELECTED')
    mode_set('OBJECT')            
    select_all('DESELECT')
    active_object(figure_name[0])
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    active_object('rig')
    bpy.ops.object.transform_apply(location=True, 
                                    rotation=True, 
                                    scale=True)
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    active_object(figure_name[0])
    objs = bpy.data.objects         
    modifier = objs[figure_name[0]].modifiers['Armature']
    objs[figure_name[0]].modifiers.remove(modifier)
    select_all('DESELECT')
    active_object('metarig')
    bpy.ops.object.delete()
    arms = bpy.data.armatures
    for blocks in arms:
        if blocks.users == 0:
            arms.remove(blocks)
    active_object('rig')
    obj = bpy.context.object
    rig_coll = obj.users_collection
    mode_set('EDIT')
    select_all('DESELECT')
    arm3 = objs['rig']
    editbones = arm3.data.edit_bones        
    for fill in rename_rig:
        oldname, newname = fill[0], fill[1]
        editbones[oldname].name = newname
    select_all('DESELECT')
    for bone in editbones:
        if (bone.name == "Foot.L"
        or bone.name == "Foot.R"):
            bone.select=True
    bpy.ops.armature.subdivide()
    editbones["Foot.L.001"].name = 'Metatarsals.L' 
    editbones["Foot.R.001"].name = 'Metatarsals.R'
    select_all('DESELECT')
    editbones['lowerTeeth'].use_deform = True
    editbones['upperTeeth'].use_deform = True
    mode_set('OBJECT')
    select_all('DESELECT')
    active_object(armature_name[0])
    bpy.ops.object.duplicate_move()
    objs[armature_name[0] + '.001'].name = 'GNSrig'
    active_object('GNSrig')
    
    # Creating Eyes Target
    mode_set("EDIT")
    select_all("DESELECT")
    obj =  bpy.context.object
    obj.data.use_mirror_x = False
    obj.data.edit_bones['Eye.L'].select= True
    mode_set("POSE")
    mode_set("EDIT")
    bpy.ops.armature.duplicate_move()
    mcheye = bpy.context.selected_editable_bones[0]
    mcheye.name = "MCH_eye"
    mcheye.head[0] = 0
    mcheye.tail[0] = 0
    bpy.ops.armature.duplicate_move(
        TRANSFORM_OT_translate={"value":(-0, -0.3, -0)})
    mcheyetrgt = bpy.context.selected_editable_bones[0]
    mcheyetrgt.name = "MCH_eyeTarget"
    bpy.ops.armature.switch_direction()
    editbones = obj.data.edit_bones
    mcheyetrgt.parent = editbones['head']
    bone_xrotation("MCH_eyeTarget", 90)
    mode_set("POSE")
    DP = 'DAMPED_TRACK'
    dp = "Damped Track"
    bone_constraint('GNSrig', 'MCH_eye', DP, dp, 'MCH_eyeTarget')
    eyes_name = ("Eye.L", "Eye.R")
    cr = "Copy Rotation"
    CR = 'COPY_ROTATION'
    for eyes in eyes_name:
        bone_constraint('GNSrig', eyes, CR, cr, 'MCH_eye', 'LOCAL')
    #objs = bpy.data.objects
    #obj.pose.bones["MCH_eyeTarget"].custom_shape = objs["WGT-rig_eyes"]

            
    # Assiging custom objects to GNSrig
    for fill in custom_objs:
        bone, widget, scale = fill[0], fill[1], fill[2]
        if len(fill) == 4:
            make_custom_object(bone+'.R', widget,scale) 
            make_custom_object(bone+'.L', widget,scale)
        else:   
            make_custom_object(bone, widget,scale)
        
    # Making a list of bones with custom object. 
    bones_list=[]
    for names in custom_objs:
        if len(names) == 4:
            bones_list.append(names[0]+'.R')
            bones_list.append(names[0]+'.L')
        else:
            bones_list.append(names[0])
            
    # Moving Bones without custom object to separate layers.
    for bones in objs['GNSrig'].data.bones:
        if bones.name not in bones_list:
            bones.layers[1] = True
            bones.layers[0] = False

    select_all('DESELECT')
    active_object(figure_name[0])
    obj = bpy.context.object
    active_object('GNSrig')
    bpy.ops.object.parent_set(type='ARMATURE_NAME')
    GNS_mod = [mod for mod in obj.modifiers 
            if mod.type == 'ARMATURE' 
            and mod.object.name == 'GNSrig']
    GNS_mod[0].name = 'GNSrig'
    GNS_mod[0].show_viewport = False
    GNS_mod[0].use_deform_preserve_volume = True
    # Resizing custom object on G3
    if figure_name[0][:8] == 'Genesis3':
        obj = bpy.context.object
        for bones in obj.pose.bones:
            if bones.name[:4] == 'Foot':
                bones.custom_shape_scale = 5
            if bones.name [:3] == 'Toe':
                bones.custom_shape_scale = 1
    
    active_object(figure_name[0]) 
    objs = bpy.data.objects
    if accessories:
        for slt in accessories:
            objs[slt].select_set(True)
            bpy.ops.object.make_links_data(type='MODIFIERS')
    bpy.ops.object.select_all(action='DESELECT')
        
    widget_coll = bpy.data.collections['Widgets']
    widget_coll.objects.link(objs['GNSrig'])
    rig_coll[0].objects.unlink(objs['GNSrig'])
    active_object(armature_name[0])
    mode_set('EDIT')
    select_all('DESELECT')    
    obj = objs[armature_name[0]]
    for bone in obj.data.edit_bones:
        if bone.name[:-2] in toebones:
            bone.select=True
    bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Z')
    obj = objs[armature_name[0]]
    for bone in obj.data.edit_bones:
        if (bone.name[:-2] in facialbones
        or bone.name in facialbones2):
            if (bone.name[:4] == 'Brow' 
            or bone.name == 'CenterBrow'):
                pass
            else:
                bone.select=True
    bpy.ops.armature.separate()
    mode_set('OBJECT')
    active_object(armature_name[0] + '.001')
    obj = bpy.context.object
    
    layers_index = list(range (33))
    while layers_index[-1] != 0:
        layers_index.pop()
        for bones in obj.data.bones:
            bones.layers[layers_index[-1]] = False
            bones.layers[24] = True
                    
    for names in deform_bones:
        obj.data.bones[names].layers[25] = True
        obj.data.bones[names].layers[24] = False
        
    select_all('DESELECT')
    active_object(armature_name[0])
    bpy.ops.object.delete()
    active_object('rig')
    objs[armature_name[0] + '.001'].select_set(True)
    bpy.ops.object.join()
    mode_set('EDIT')
    select_all('DESELECT') 
    obj = bpy.context.object
    editbones = obj.data.edit_bones         
    if armature_name[0][:8] != 'Genesis8':
        editbones['Heel.R'].parent = editbones['Foot.R']        
        editbones['Heel.L'].parent = editbones['Foot.L']
    for tb in toebones:
        if tb[-2] != '_':
            editbones[tb + '.R']. parent = editbones['Metatarsals.R']
            editbones[tb + '.L']. parent = editbones['Metatarsals.L']
    BRT = [brt for brt in editbones 
            if brt.name[:10] == 'ORG-breast' 
            or brt.name[:6] == 'breast']
    for bone in BRT:
        bone.parent =  editbones['ORG-spine.008']
    for bone in editbones:
        if bone.name in FaceHeadParent:
            bone.parent = editbones['head']
    mode_set('POSE')
    obj = bpy.context.object
    for bone in obj.pose.bones:
        if (bone.name[:-2] in facialbones 
        or bone.name in facialbones2):
            if (bone.name[:5] == 'lower' 
            or bone.name == 'upperFaceRig'):
                pass
            else:
                if bone.name:
                    posebones = obj.pose.bones
                    posebones[bone.name].bone_group_index = 3
                    shape = objs["WGT-rig_brow.T.L"]
                    posebones[bone.name].custom_shape = shape
    
    cr = "Copy Rotation"
    CR = 'COPY_ROTATION'
    l, r = '.L', '.R'
    for tb in toebones:
        if tb[-2] != '_':
            toe = "ORG-toe"
            bone_constraint('rig', tb+r, CR, cr, toe+r, 'LOCAL')
            bone_constraint('rig',tb+l, CR, cr, toe+l, 'LOCAL')
            posebones = obj.pose.bones
            posebones[tb+r].constraints[cr].use_z = False
            posebones[tb+l].constraints[cr].use_z = False
            posebones[tb+r].constraints[cr].invert_x = True
            posebones[tb+l].constraints[cr].invert_x = True
            posebones[tb+r].constraints[cr].invert_y = True
            posebones[tb+l].constraints[cr].invert_y = True
    
    for bb in browbones:
        cl =  "Copy Location"
        CL = 'COPY_LOCATION'
        rbrow = "brow.B.R.002"
        lbrow = "brow.B.L.002"
        if bb[-1] == 'R':
            bone_constraint('rig',bb, CL, cl, rbrow, 'LOCAL')
        else:
            bone_constraint('rig',bb, CL, cl, lbrow, 'LOCAL')
        posebones[bb].constraints[cl].influence = 0.6      

    dt = "Damped Track"
    DT = 'DAMPED_TRACK'
    bone_constraint('rig','lowerJaw', CR, cr, "MCH-jaw_master", 'LOCAL')
    bone_constraint('rig','Eye.L', DT, dt, "MCH-eye.L.001")
    bone_constraint('rig','Eye.R', DT, dt, "MCH-eye.R.001")         
    constraints_influence(bones_influence)
    for bone in posebones:    
        if bone.name[:-2] in eyebones:
            cnstrnts = [c for c in bone.constraints
            if c.type == DT or 'STRETCH_TO']
            for c in cnstrnts:
                bone.constraints.remove(c)
                
    bpy.data.texts['rig_ui.py'].cursor_set(1732)
    bpy.data.texts['rig_ui.py'].write("        \
row.prop(context.active_object.data, 'layers', \
index=24, toggle=True, text='Face (Tertiary)') \n")
    bpy.data.texts['rig_ui.py'].as_module()

    for num in range(32):
        if (num != 0 
        and num != 3 
        and num != 5 
        and num != 7 
        and num != 10 
        and num != 13 
        and num != 16):
            obj.data.layers[num] = False
    mode_set('OBJECT') 
    select_all('DESELECT')
    active_object(figure_name[0] + '.001')
    active_object(figure_name[0])
    bpy.ops.object.join()
    if accessories:
        for slt in accessories:
            objs[slt].select_set(True)
            active_object('rig')
            bpy.ops.object.parent_set(type='ARMATURE_NAME')
            select_all('DESELECT')
            active_object(figure_name[0])
            obj = bpy.context.object
            obj.modifiers[-1].use_deform_preserve_volume = True
            bpy.ops.object.modifier_move_to_index(modifier="Armature", index=0)
            objs[slt].select_set(True)
            bpy.ops.object.make_links_data(type='MODIFIERS')
            select_all('DESELECT')
    else:
        active_object('rig')
        bpy.ops.object.parent_set(type='ARMATURE_NAME')
        select_all('DESELECT')
        active_object(figure_name[0])
        obj = bpy.context.object
        obj.modifiers[-1].use_deform_preserve_volume = True
        bpy.ops.object.modifier_move_to_index(modifier="Armature", index=0)
        select_all('DESELECT')                     
    active_object('rig')
    obj = bpy.context.object
    obj.show_in_front = True
    mode_set('POSE')
    bpy.ops.pose.armature_apply()
