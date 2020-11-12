import bpy

from mathutils import Vector
from bpy.props import EnumProperty, IntProperty, FloatProperty

import var
from lipsync import (
                    create_lipsync,
                    add_lip_ctrlr,
                    remove_lip_ctrlr,
                    configure_lipsync,
                    apply_lipsync,
                    update_custom_shape
)
from mixamo import (
                    mixamo_copy, 
                    mixamo_remove,
                    bake_mixamo,
                    enable_GNSrig,
                    disable_GNSrig,
                    adjust_framelength,
)
from utils import (
                    initialize,
                    rig_match,
					sorting_objects,
                    sorting_armature,
                    add_metarig,
                    rig_genesis_figure,
                    generate_rig,
                    empty_name_holders,
                    armature_name, 
                    figure_name, 
                    accessories, 
                    INPUT_ERR, 
                    ERROR, 
                    SUCCESS, 
                    active_object, 
                    convert_to_mixamo
)

def mixamo_keyframes(index1, index2):
    global fcurve1, fcurve2, kf_p1, kf_p2, framelength
    kf_p1 = []
    kf_p2 = []
    if not armature_name:
        sorting_armature()
    objs = bpy.data.objects
    action = objs[armature_name[0]].animation_data.action
    fcurve =  list(action.fcurves)
    for fc in fcurve:
        keyframes = list(fc.keyframe_points)   
    framelength = len(keyframes)
    for fr in range(framelength):
        fcurve1 = action.fcurves[index1]
        fcurve2 = action.fcurves[index2]
        kf_p1.append(fcurve1.keyframe_points[fr].co[1])
        kf_p2.append(fcurve2.keyframe_points[fr].co[1])
        
def tilt_values(a,b,c,d):
    widget_items = list(bpy.data.collections['Widgets'].objects)
    for i in widget_items:
        if i.name[:8] == 'Armature':
            mixamo_keyframes(a,a)
        elif i.name[:8] == 'Genesis2':
            mixamo_keyframes(b,b)
        elif i.name[:8] == 'Genesis3':
            mixamo_keyframes(c,c)
        elif i.name[:8] == 'Genesis8':
            mixamo_keyframes(d,d)

def tilt_values2(a,b,c,d,e,f,g,h):
    widget_items = list(bpy.data.collections['Widgets'].objects)
    for i in widget_items:
        if i.name[:8] == 'Armature':
            mixamo_keyframes(a,b)
        elif i.name[:8] == 'Genesis2':
            mixamo_keyframes(c,d)
        elif i.name[:8] == 'Genesis3':
            mixamo_keyframes(e,f)
        elif i.name[:8] == 'Genesis8':
            mixamo_keyframes(g,h)
            
class OBJECT_OT_Initialize(bpy.types.Operator):
    """Generates rigify rig from active Genesis armature"""
    
    bl_label = "Initialize"
    bl_idname = "object.initialize"
    bl_options = {'UNDO', 'INTERNAL'}
    
    @classmethod
    def poll(cls, context):
        try:
            for obj in bpy.data.objects:
                return (obj.users > 0 and \
                bpy.context.object.data.layers_protected[31] == False)
        except:
            return{'CANCELLED'}
    
    def execute(self, context):
        try:
            result = initialize()
            if result[0] == SUCCESS:
                pass
            else:
                self.report(type = {result[0]}, message = result[1])
            return {'FINISHED'}
        except:
            return {"CANCELLED"}
        
    
class OBJECT_OT_AddMetarig(bpy.types.Operator):
    """ Add metarig"""
    bl_label = "Add metarig"
    bl_idname = "object.metarig_add"
    bl_options = {'UNDO', 'INTERNAL'}
    
    @classmethod
    def poll(cls, context):
        try:
            arm = [a for a in bpy.data.objects if a.name[:7] == 'Genesis' and a.type == 'ARMATURE']
            return (len(arm) > 0 and bpy.context.object.data.layers_protected[30] == True)
        except:
            pass
    
    def execute(self, context):
        try:
            add_metarig()
        except:
            self.report({ERROR}, var.except_msg[0])
        return {'FINISHED'}

class OBJECT_OT_MatchRig(bpy.types.Operator):
    """ Match metarig to Genesis Figure"""
    bl_label = "Match Rig"
    bl_idname = "object.match_rigs"
    bl_options = {'UNDO', 'INTERNAL'}
    
    @classmethod
    def poll(cls, context):
        try:
            arm = [a for a in bpy.data.objects if a.name == 'metarig']
            return (len(arm) > 0 and bpy.context.object.data.layers_protected[29] == True)
        except:
            pass
    
    def execute(self, context):
        rig_match()
        return {'FINISHED'}
    
    
class OBJECT_OT_GenerateRig(bpy.types.Operator):
    """ Generates rigify rig from active metarig"""
    bl_label = "Generate Rig"
    bl_idname = "object.generate_rig"
    bl_options = {'UNDO', 'INTERNAL'}
    
    @classmethod
    def poll(cls, context):
        try:
            arm = [a for a in bpy.data.objects if a.name == 'metarig']
            return (len(arm) > 0 and bpy.context.object.data.layers_protected[28] == True)
        except:
            pass

    def execute(self, context):
        generate_rig()
        return {'FINISHED'}     
      
        
class OBJECT_OT_RigGenesisFigure(bpy.types.Operator):
    ''' Generates rigify rig from active Genesis armature'''
    bl_label = "Rig Figure"
    bl_idname = "object.rig_genesis_figure"
    bl_options = {'UNDO', 'INTERNAL'}
    
    @classmethod
    def poll(cls, context):
        try:
            arm = [a for a in bpy.data.objects if a.name == 'rig']
            return (len(arm) > 0 and bpy.context.object.data.layers_protected[27])
        except:
            pass
        
    def execute(self, context):
        rig_genesis_figure()
        return {'FINISHED'}


class OBJECT_OT_HelpNote(bpy.types.Operator):
    """Generates rigify rig from active Genesis armature"""
    bl_label = "Addon Guide"
    bl_idname = "object.help_note"
    bl_options = {'UNDO', 'INTERNAL'}
    
    def invoke(self, context, event):
        message = ( "   ADDON GUIDE:\n \
1.     Launch DAZstudio software and export genesis figure (genesis 3 or genesis 8) as an FBX file.\n \
        \n\
2.     In blender, use the import button to import the FBX file. But while still in the import menu,\n \
        ensure 'Use Pre/Post Rotation' is unchecked (found under 'Transforms'). And also ensure \n \
        'Automatic Bone Orientation' is checked (found  under 'Armature') \n \
        \n \
3.     With the Genesis armature selected, start the rigging process by selecting 'Initialize' button,\n \
        then 'Add metarig' button, then 'Match metarig' button, then 'Generate rig' button, and finally, \n \
        select the 'Rig figure' Button.\n \
        \n \
4.     Once rigging process is completed, Adobe mixamo animation templates can be added to the figure: \n \
        -  First, visit mixamo.com and download any animation template in FBX format. \n \
        -  Import the FBX file into the blender scene and select 'Bind' button and then the 'Play' button. \n \
        -  When no longer needed, select 'Remove' button to remove the animation armature from scene."
    )
        self.report({'ERROR'}, message)
        return {'FINISHED'}
    
class OBJECT_OT_ConvertToMixamo(bpy.types.Operator):
    """ Convert Genesis figure to Mixamo armature"""
    bl_label = "Genesis to Mixamo"
    bl_idname = "object.convert_mixamo"
    bl_options = {'UNDO', 'INTERNAL'}
    
    @classmethod
    def poll(cls, context):
        try:
            return (bpy.context.object.type == 'ARMATURE' 
        and bpy.context.object.name[:7] == 'Genesis'
        or bpy.context.object.name[:5] == 'Donor')
        except:
            return{'CANCELLED'}
        
    def execute(self, context):
        try:
            result = convert_to_mixamo()
            if result[0] == SUCCESS:
                pass
            else:
                self.report(type = {result[0]}, message = result[1])
            return {'FINISHED'}
        except:
            return{'CANCELLED'}
    
    
class OBJECT_OT_MixamoCopy(bpy.types.Operator):
    """ Import Adobe Mixamo Armature (FBX file) into scene and copy animation with this button"""
    bl_label = "Copy Mixamo"
    bl_idname = "object.copy_mixamo"
    bl_options = {'UNDO', 'INTERNAL'}
    
    @classmethod
    def poll(cls, context):
        try:
            animgns = [ob for ob in bpy.data.objects 
            if ob.type == 'ARMATURE' 
            and (ob.name[:7] == 'Genesis' and ob.children)]
            return bpy.context.object.type == 'ARMATURE' and len(animgns) < 1
        except:
            return{'CANCELLED'}
        
    def execute(self, context):
        result = mixamo_copy()
        if result[0] == SUCCESS:
            return {'FINISHED'}
        else:
            self.report(type = {result[0]}, message = result[1])
            return {'FINISHED'}
    
    
class OBJECT_OT_RemoveMixamo(bpy.types.Operator):
    """ Remove bone constraints copying Mixamo transform"""
    bl_label = "Remove Mixamo"
    bl_idname = "object.remove_mixamo"
    bl_options = {'UNDO', 'INTERNAL'}
    
    @classmethod
    def poll(cls, context):
        try:
            arma = [ob.name for ob in bpy.data.armatures
                if ob.name[:8] == 'Armature' 
                or ob.name[:7] == 'Genesis']
            gnsarma = [ob.name for ob in bpy.data.objects
                if ob.name == 'GNSrig']
            return arma and gnsarma and len(bpy.data.armatures) > 2
        except:
            pass
        
    def execute(self, context):
        try:
            mixamo_remove()
            return {'FINISHED'}
        except:
            return {'FINISHED'}

class OBJECT_OT_BakeMixamo(bpy.types.Operator):
    """ Bakes Mixamo Animation to GNSrig"""
    bl_label = "Bake Animation"
    bl_idname = "object.mixamo_bake"
    bl_options = {'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        try:
            animdata = [ad for ad in bpy.data.actions 
            if ad.name[:8] == 'Armature'
            or ad.name[:7] == 'Genesis'
            or ad.name[:5] == 'Donor']
            return (bpy.context.object.name == "GNSrig"
                    and len(animdata) > 0 
                    and len(bpy.data.armatures) > 2
                    )
        except:
            pass
        
    def execute(self, context):
        bake_mixamo()
        return {'FINISHED'}
    
       
class Poll:
    bl_options = {'UNDO', 'INTERNAL'}
    @classmethod
    def poll(cls, context):
        try:
            if bpy.data.actions:
                    animdata = [ad for ad in bpy.data.actions 
                    if ad.name[:8] == 'Armature'
                    or ad.name[:7] == 'Genesis'
                    or ad.name[:5] == 'Donor']
            else:
                animdata = ''
            return len(animdata) > 0 and bpy.context.object.name == 'GNSrig'
        except:
            pass
        
class modality:
    first_mouse_y: IntProperty()

    def modal(self, context, event):
        if event.type == 'MOUSEMOVE':
            bpy.context.window.cursor_set("SCROLL_Y")
            delta = self.first_mouse_y - event.mouse_y
            mouse_move = delta * 0.005 
            winman = bpy.data.window_managers["WinMan"].adjust_mixam.mixam_bones
            for fr in range(framelength):
                a = fcurve1.keyframe_points[fr]
                b = fcurve2.keyframe_points[fr]
                if winman == 'larm_bone' or winman == 'thigh_bone':
                    a.co[1] = kf_p1[fr] - mouse_move
                    b.co[1] = kf_p2[fr] + mouse_move
                else:
                    a.co[1] = kf_p1[fr] + mouse_move
                    b.co[1] = kf_p2[fr] + mouse_move
                
        elif event.type == 'LEFTMOUSE':
            bpy.context.window.cursor_set("DEFAULT")
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.context.window.cursor_set("DEFAULT")
            for fr in range(framelength):
                fcurve1.keyframe_points[fr].co[1] = kf_p1[fr]
                fcurve2.keyframe_points[fr].co[1] = kf_p2[fr]
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}
    
class OBJECT_OT_AdjustHead(Poll, modality, bpy.types.Operator):
    """Adjust the arm rotation of GNSrig"""
    bl_label = "Adjust Head"
    bl_idname = "object.adjust_head_pos"

    def invoke(self, context, event):
        tilt_values(54, 244, 924, 904)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
class OBJECT_OT_AdjustNeck(Poll, modality, bpy.types.Operator):
    """Adjust the Neck rotation of GNSrig"""
    bl_label = "Adjust Neck"
    bl_idname = "object.adjust_neck_pos"
    
    def invoke(self, context, event):
        tilt_values(44, 234, 904, 884)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
           
class OBJECT_OT_AdjustArm(Poll, modality, bpy.types.Operator):
    """Adjust the arm rotation of GNSrig"""
    bl_label = "Adjust Arms"
    bl_idname = "object.adjust_arm_pos"
       
    def invoke(self, context, event):
        tilt_values2(266, 76, 376, 586, 666, 416, 646, 396)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
    
class OBJECT_OT_AdjustLowerArm(Poll, modality, bpy.types.Operator):
    """Adjust the lower arm rotation of GNSrig"""
    bl_label = "Adjust lower arm"
    bl_idname = "object.adjust_lower_arm_pos"

    def invoke(self, context, event):
        tilt_values2(274, 84, 384, 594, 684, 434, 664, 414)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
     
class OBJECT_OT_AdjustHand(Poll, modality, bpy.types.Operator):
    """Adjust the Hand rotation of GNSrig"""
    bl_label = "Adjust Hand"
    bl_idname = "object.adjust_hand_pos"

    def invoke(self, context, event):
        tilt_values2(286, 96, 396, 606, 706, 456, 684, 434)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
        
class OBJECT_OT_AdjustShoulder(Poll, modality, bpy.types.Operator):
    """Adjust the shoulder rotation of GNSrig"""
    bl_label = "Adjust Shoulder"
    bl_idname = "object.adjust_shoulder_pos"
        
    def invoke(self, context, event):
        tilt_values2(256, 66, 366, 576, 656, 406, 636, 386)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

class OBJECT_OT_AdjustTorso(Poll, modality, bpy.types.Operator):
    """Adjust the torso rotation of GNSrig"""
    bl_label = "Adjust Torso"
    bl_idname = "object.adjust_torso_pos"
        
    def invoke(self, context, event):
        tilt_values(14, 204, 374, 344)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

class OBJECT_OT_AdjustThigh(Poll, modality, bpy.types.Operator):
    """Adjust the Thigh rotation of GNSrig"""
    bl_label = "Adjust Thigh"
    bl_idname = "object.adjust_thigh_pos"
        
    def invoke(self, context, event):
        tilt_values2(486, 446, 116, 26, 196, 26, 186, 26)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
class OBJECT_OT_AdjustShin(Poll, modality, bpy.types.Operator):
    """Adjust the Shin rotation of GNSrig"""
    bl_label = "Adjust Shin"
    bl_idname = "object.adjust_shin_pos"
        
    def invoke(self, context, event):
        tilt_values2(494, 454, 124, 34, 214, 44, 204, 44)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
    
class OBJECT_OT_AdjustFoot(Poll, modality, bpy.types.Operator):
    """Adjust the Foot rotation of GNSrig"""
    bl_label = "Adjust Foot"
    bl_idname = "object.adjust_foot_pos"
        
    def invoke(self, context, event):
        tilt_values2(504, 464, 134, 44, 224, 54, 224, 64)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
class OBJECT_OT_AdjustToe(Poll, modality, bpy.types.Operator):
    """Adjust the Toe rotation of GNSrig"""
    bl_label = "Adjust Toe"
    bl_idname = "object.adjust_toe_pos"
        
    def invoke(self, context, event):
        tilt_values2(514, 474, 144, 54, 244, 74, 234, 74)
        self.first_mouse_y = event.mouse_y
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    
class OBJECT_OT_Create_Lipsync(bpy.types.Operator):
    """ Creates control bones for lips synchronization"""
    bl_label = "Create Controllers"
    bl_idname = "object.create_lipsync"
    bl_options = {'UNDO', 'INTERNAL'}
    
    @classmethod
    def poll(cls, context):
        try:
            obj = [ob for ob in bpy.data.objects
                    if ob.name == 'Arrow']
            return len(obj) < 1
        except:
            pass
        
    def execute(self, context):
        result = create_lipsync()
        if result[0] == SUCCESS:
            pass
        else:
            self.report(type = {result[0]}, message = result[1])
        return {'FINISHED'}
    
    
class OBJECT_OT_AddLipsControl(bpy.types.Operator):
    """ Add new lip controller bone"""
    bl_label = "New Controller"
    bl_idname = "object.addlipctrl"
    
    @classmethod
    def poll(cls, context):
        try:
            obj = [ob for ob in bpy.data.objects
                    if ob.name == 'Arrow']
            return (obj and context.mode == 'POSE' 
            and context.object.data.layers_protected[30] == False)
        except:
            pass
        
    def execute(self, context):
        add_lip_ctrlr()
        return {'FINISHED'}
    
 
class OBJECT_OT_RemoveLipsControl(bpy.types.Operator):
    """ Remove selected lip controller bone"""
    bl_label = "Remove Controller"
    bl_idname = "object.removelipctrl"
    
    @classmethod
    def poll(cls, context):
        try:
            a = ''
            if context.selected_pose_bones:   
                a = [bone.custom_shape for bone in context.selected_pose_bones
                        if bone.custom_shape.name[:4] == 'Text']
            return a
        except:
            pass
        
    def execute(self, context):
        remove_lip_ctrlr()
        return {'FINISHED'}
    
        
class OBJECT_OT_Configure_Lipsync(bpy.types.Operator):
    """ Configures lips synchronization"""
    bl_label = "Configure Lip sync"
    bl_idname = "object.configure_lipsync"
    bl_options = {'REGISTER', 'UNDO'}

    
    mode : EnumProperty(items =  [
            ('EDIT', 'Modify in Edit mode', 'Deform figure in Edit mode', 'EDITMODE_HLT', 1),
            ('SCULPT', 'Modify in Sculpt mode', 'Deform figure in Sculpt mode', 'SCULPTMODE_HLT', 2),
            ('POSE', 'Modify in Pose mode', 'Deform figure in Pose mode', 'POSE_HLT', 3),],
                        name = 'Mode',
                        description= "Select mode in which to deform the figure",
    )

    @classmethod
    def poll(cls, context):
        a = ''
        if context.selected_pose_bones:   
            a = [bone.custom_shape for bone in context.selected_pose_bones
                    if bone.custom_shape.name[:4] == 'Text']
        return a
        
    def execute(self, context):
        configure_lipsync(self.mode)
        return {'FINISHED'}
    
        
class OBJECT_OT_Apply_Lipsync(bpy.types.Operator):
    """ Applies lips synchronization"""
    bl_label = "Apply Lip sync"
    bl_idname = "object.apply_lipsync"
    
    @classmethod
    def poll(cls, context):
        try:
            if (context.object.name == context.scene.main_tool.meshes 
            or context.object.name == context.scene.main_tool.armatures):
                for obj in bpy.data.objects:
                    return (context.object.use_shape_key_edit_mode == True
                    or context.object.data.layers_protected[30] == True
                    and obj.name == 'Arrow')
        except:
            pass

    def execute(self, context):
        apply_lipsync()
        return {'FINISHED'}
    
    
class OBJECT_OT_CustomShapeUpadate(bpy.types.Operator):
    """Updates name of custom shape"""
    bl_label = "Update"
    bl_idname = "object.upd_cstmshp"
    
    @classmethod
    def poll(cls, context):
        try:
            a = ''
            if context.selected_pose_bones:   
                a = [bone.custom_shape for bone in context.selected_pose_bones
                        if bone.custom_shape.name[:4] == 'Text']
            return a
        except:
            pass
    
    def execute(self, context):
        update_custom_shape()
        return{'FINISHED'}


class OBJECT_OT_ResetBone(bpy.types.Operator):
    """Apply location of selected bone as reset"""
    bl_label = "Apply Reset Bone"
    bl_idname = "object.reset_bone"
    
    @classmethod
    def poll(cls, context):
        try:
            obj = context.selected_pose_bones
            a = ''
            if obj[0].location != Vector((0,0,0)):
                a = [bone.custom_shape for bone in context.selected_pose_bones
                        if bone.custom_shape.name[:4] == 'Text']
            return a
        except:
            pass
    
    def execute(self, context):
        bpy.ops.pose.armature_apply(selected=True)
        return{'FINISHED'}
    
##############################################################    
class OBJECT_OT_SwitchArmature(bpy.types.Operator):
    """Switch between rig and GNSrig"""
    bl_label = "Addon Guide"
    bl_idname = "object.switch_armature"
    
    def execute(self, execute):
        if not figure_name:
            sorting_objects()
        objs = bpy.data.objects
        for mod in objs[figure_name[0]].modifiers:
            if (mod.type == "ARMATURE" 
            and mod.object.name == "GNSrig"):
                if mod.show_viewport == True:
                    active_object('rig')
                    disable_GNSrig()
                else:
                    enable_GNSrig()
        return {'FINISHED'}

class OBJECT_OT_MatchFrame(bpy.types.Operator):
    """ Adjust frame length to match key length"""
    bl_label = "Match Frame"
    bl_idname = "object.match_frame"
    
    @classmethod
    def poll(cls, context):
        try:
            return bpy.context.object.animation_data.action.fcurves
        except:
            pass
        
    def execute(self, context):
        adjust_framelength()
        return {'FINISHED'}

classes = [ 
            OBJECT_OT_Initialize, 
            OBJECT_OT_AddMetarig, 
            OBJECT_OT_MatchRig, 
            OBJECT_OT_GenerateRig, 
            OBJECT_OT_RigGenesisFigure, 
            OBJECT_OT_HelpNote,
            OBJECT_OT_ConvertToMixamo,
            OBJECT_OT_MixamoCopy, 
            OBJECT_OT_RemoveMixamo, 
            OBJECT_OT_BakeMixamo, 
            OBJECT_OT_SwitchArmature, 
            OBJECT_OT_AdjustHead, 
            OBJECT_OT_AdjustNeck,
            OBJECT_OT_AdjustShoulder,
            OBJECT_OT_AdjustArm,
            OBJECT_OT_AdjustLowerArm,
            OBJECT_OT_AdjustHand,
            OBJECT_OT_AdjustTorso, 
            OBJECT_OT_AdjustThigh,
            OBJECT_OT_AdjustShin,
            OBJECT_OT_AdjustFoot,
            OBJECT_OT_AdjustToe,
            OBJECT_OT_MatchFrame, 
            OBJECT_OT_Create_Lipsync,
            OBJECT_OT_AddLipsControl,
            OBJECT_OT_RemoveLipsControl,
            OBJECT_OT_Configure_Lipsync,
            OBJECT_OT_Apply_Lipsync,
            OBJECT_OT_CustomShapeUpadate,
            OBJECT_OT_ResetBone,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        