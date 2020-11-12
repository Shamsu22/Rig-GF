# ##### BEGIN GPL LICENSE BLOCK #####
# Rig-GNS is a blender addon for rigging Genesis figures from DAZ studio in Blender.
# Copyright (c) 2020, Shamsuddin Sulaiman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Rig-GNS",
    "version": (0, 2, 0),
    "author": "Shamsu Ddin",
    "blender": (2, 83, 0),
    "description": "Rig Genesis figures from DAZ studio in Blender",
    "location": "Armature properties, View3d tools panel",
    "wiki_url": "https://22722studios.blogspot.com/2020/07/rig-gns-add-on.html",
    "category": "Rigging"}
    
import bpy
import os
from mathutils import Vector
import operators
import var

from bpy.types import (
    PropertyGroup,
    WindowManager
    )
from bpy.props import (
    EnumProperty,
    BoolProperty,
    PointerProperty,
    StringProperty,
    FloatProperty,
    CollectionProperty
    )
from lipsync import(
    scene_armatures,
    scene_meshes
)
preview_collections = {}

icon_thumbnails = (
    'lips', 'adjust', 'rig', 'init', 'match', 'metarig', 
    'mixamo', 'bake', 'bind'
)

def thumb_image():
    import bpy.utils.previews
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")
    for t in icon_thumbnails:
        pcoll = bpy.utils.previews.new()
        pcoll.load(t +"_icon", os.path.join(icons_dir, t+".png"), 'IMAGE')
        preview_collections[t] = pcoll


class AdjustBones(PropertyGroup):
    enable_gns : BoolProperty(
        name="Use GNSrig",
        description = "Enable GNSrig",
        default = False
        )

    mixam_bones: EnumProperty(
            name="Adjust Mixamo",
            items=var.list_bones,
            description="",
            default='head_bone'
            )
            
            
class SceneProperties(PropertyGroup):      
    armatures : EnumProperty(
        name="Armature:",
        description="Apply Data to attribute.",
        items=scene_armatures
    )
    meshes : EnumProperty(
        name="Meshes:",
        description="Apply Data to attribute.",
        items=scene_meshes,
    )
    name : StringProperty(
    )
    driverbonestore : StringProperty(
    )
    figheightstore : FloatProperty(
    )
    auto_modify: BoolProperty(name="Auto Modify")

class RigGNS:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Rig GNS'
    
    
class VIEW3D_MT_DeformationMode(RigGNS, bpy.types.Menu):
    bl_idname = "VIEW3D_MT_DeformationMode"
    bl_label = "Choose Mode"

    def draw(self, context):
        pie = self.layout.menu_pie()  
        pie.operator_enum('object.configure_lipsync', "mode")
         
    
class VIEW3D_PT_RigGenesis(RigGNS, bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Rig Genesis"
    
    @classmethod
    def poll(cls, context):
        return bpy.context.mode == 'OBJECT' or bpy.context.mode == 'POSE'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.scale_y = 1.5
        row.operator("import_scene.fbx", text = 'Import Armature', icon='IMPORT')
        layout.label(text="Rig Buttons:")
        split = layout.split(align=True)
        col = split.column(align=True)

        pcoll = preview_collections["init"]
        init_icon = pcoll["init_icon"]
        col.operator("object.initialize", icon_value=init_icon.icon_id)

        pcoll = preview_collections["match"]
        match_icon = pcoll["match_icon"]
        col.operator("object.match_rigs", icon_value=match_icon.icon_id)
        
        pcoll = preview_collections["metarig"]
        metarig_icon = pcoll["metarig_icon"]

        col = split.column(align=True)
        col.operator("object.metarig_add", icon_value=metarig_icon.icon_id)
        col.operator("object.generate_rig", icon='POSE_HLT')

        pcoll = preview_collections["rig"]
        rig_icon = pcoll["rig_icon"]
        
        row = layout.row()
        row.operator("object.rig_genesis_figure", icon_value=rig_icon.icon_id)

class VIEW3D_PT_HelpButtons(RigGNS, bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Help"
    bl_parent_id = "VIEW3D_PT_RigGenesis"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        box = layout.box()
        row = box.row()
        sub = row.row(align = True)
        sub.operator("object.help_note", text = 'Info', icon='INFO')

class VIEW3D_PT_Animation(RigGNS, bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Animations"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return bpy.context.mode == 'OBJECT' or bpy.context.mode == 'POSE'

    def draw(self, context):
        adjust_mixam = context.window_manager.adjust_mixam
        
        layout = self.layout
        
        links = 'http://www.mixamo.com/'

        try:
            st = context.object.animation_data
            action_name = [a.name for a in bpy.data.actions 
                            if a.name[:6] == 'Action']
            if bpy.data.objects['GNSrig'].animation_data.action and action_name:
                row = layout.row()
                row.template_ID(st, "action")
        except:
            pass
        
        pcoll = preview_collections["mixamo"]
        mixamo_icon = pcoll["mixamo_icon"]
        
        row = layout.row(align=True)
        row.operator("import_scene.fbx", text = '', icon='IMPORT')
        row.label(text="") 
        row.label(text="Get Mixamo:")      
        row.operator('wm.url_open', text='', 
                     icon_value=mixamo_icon.icon_id).url = links

        row = layout.row()
        animgns = [ob for ob in bpy.data.objects 
            if ob.type == 'ARMATURE' 
            and (ob.name[:7] == 'Genesis' and ob.children)]
        animgns2 = [ob for ob in bpy.data.objects 
            if ob.type == 'ARMATURE' 
            and (ob.name[:5] == 'Donor')]
        gnsarma = [ob for ob in bpy.data.objects 
            if ob.name == 'GNSrig']
        if animgns or animgns2 and gnsarma:
            row.operator("object.convert_mixamo",
                            text = 'Convert to Mixamo',
                            icon_value=mixamo_icon.icon_id)

        split = layout.split(align=True)
        pcoll = preview_collections["bind"]
        bind_icon = pcoll["bind_icon"]
        col = split.column(align=True)
        col.operator("object.copy_mixamo", 
                        text = 'Bind', 
                        icon_value=bind_icon.icon_id)

        col = split.column(align=True)
        col.operator("object.remove_mixamo",
                        text = 'Remove', 
                        icon='CANCEL')
            
        pcoll = preview_collections["bake"]
        bake_icon = pcoll["bake_icon"]
        row = layout.row()
        row.operator("object.mixamo_bake", 
                        text = 'Bake Animation',
                        icon_value=bake_icon.icon_id)
            
        layout.separator()
        pcoll = preview_collections["adjust"]
        adjust_rig = pcoll["adjust_icon"]

        row = layout.row(align=True)  
        row.prop(adjust_mixam, 'mixam_bones', text ='Bone', icon_value=adjust_rig.icon_id)
        if adjust_mixam.mixam_bones == 'head_bone':
            row.operator("object.adjust_head_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'neck_bone':
            row.operator("object.adjust_neck_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'shoulder_bone':
            row.operator("object.adjust_shoulder_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'uarm_bone':
            row.operator("object.adjust_arm_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'larm_bone':
            row.operator("object.adjust_lower_arm_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'hand_bone':
            row.operator("object.adjust_hand_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'torso_bone':
            row.operator("object.adjust_torso_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'thigh_bone':
            row.operator("object.adjust_thigh_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'shin_bone':
            row.operator("object.adjust_shin_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'foot_bone':
            row.operator("object.adjust_foot_pos", text = '', icon_value=adjust_rig.icon_id)
        elif adjust_mixam.mixam_bones == 'toe_bone':
            row.operator("object.adjust_toe_pos", text = '', icon_value=adjust_rig.icon_id)

        layout.separator()   
        row = layout.row(align=True)

        objs = bpy.data.objects
        sign = 'BLANK1'
        for meshes in objs:
            if meshes.name[:7] == 'Genesis':
                for mod in meshes.modifiers:
                    if (mod.type == "ARMATURE" 
                    and mod.object.name == "GNSrig"):
                        if mod.show_viewport == True:
                            sign = 'CHECKBOX_HLT'
                        else:
                            sign = 'CHECKBOX_DEHLT'

        row.operator("object.switch_armature", text = '', icon = sign)
        row.label(text = 'GNSrig')

        try:
            if bpy.data.actions:
                st = context.object.animation_data
                arma = context.object
                if arma.name [:7] != 'Genesis' or arma.name[:8] != 'Armature':
                    row = layout.row(align=True)
                    row.template_ID(st, "action")
        except:
            st = context.object.animation_data
            row = layout.row()
            row.template_ID(st, "action")
        row.operator("object.match_frame", text='', icon='PREVIEW_RANGE')
            
class VIEW3D_PT_LipSync(RigGNS, bpy.types.Panel):
    """Control buttons for lip-sync"""
    bl_label = "Lip-Sync"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'OBJECT' or context.mode == 'EDIT_MESH' 
                or context.mode == 'SCULPT' or context.mode == 'POSE')
    
    def draw(self, context):
        scene = context.scene
        maintools = scene.main_tool
        
        layout = self.layout
        #layout.use_property_split = True
        flow = layout.grid_flow()
        col = flow.column()

        col.prop(maintools, "armatures", text="", icon="ARMATURE_DATA")
        col.prop(maintools, "meshes", text="", icon="OUTLINER_DATA_MESH")
        
        pointer = []
        pointer = [obj.name for obj in bpy.data.objects if obj.name == 'Arrow']
        
        if pointer:
            layout.label(text='')
            layout.label(text='Scale controllers for effect!', icon='INFO')
        else:
            layout.separator()
            pcoll = preview_collections["lips"]
            lips_icon = pcoll["lips_icon"]
                   
            row = layout.row()
            row.operator("object.create_lipsync", 
                            text = 'Create Controllers',
                            icon_value=lips_icon.icon_id)  
            
            tool = context.scene.main_tool
            row = layout.row()
            row.prop(tool,'auto_modify')
           
class VIEW3D_PT_LipSync_Configuraton(RigGNS, bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Controllers Settings"
    bl_parent_id = "VIEW3D_PT_LipSync"
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'OBJECT' or context.mode == 'EDIT_MESH' 
                or context.mode == 'SCULPT' or context.mode == 'POSE')
    
    def draw(self, context):
        layout = self.layout        
        split = layout.split(align=True)
        col = split.column(align=True)
        col.operator("object.addlipctrl", text = 'New', icon='ADD')
        col = split.column(align=True)
        col.operator("object.removelipctrl", text = 'Remove', icon='REMOVE')
        
        layout.separator()
        for obj in bpy.data.objects:
            if obj.name == 'Arrow':
                if (context.object.name == context.scene.main_tool.meshes 
                and context.object.use_shape_key_edit_mode == True):
                    msg = 'Modify between Edit and Sculpt Mode'
                    row = layout.row(align=True) 
                    row.label(text=msg, icon = 'INFO')
                elif (context.object.name == context.scene.main_tool.armatures
                and context.object.data.layers_protected[30] == True):
                    msg = 'Modify only in Pose Mode'
                    row = layout.row(align=True) 
                    row.label(text=msg, icon = 'INFO')
        
        split = layout.split(align=True)
        row = split.row(align=True) 
        row.label(text='Modify figure:')
        row.menu('VIEW3D_MT_DeformationMode', text = 'Select Mode')
        
        split = layout.split(align=True)
        row = split.row(align=True) 
        row.label(text='')
        row.operator("object.apply_lipsync", text = 'Apply', icon='CHECKMARK')
        
        layout.separator()
        scene = context.scene
        maintools = scene.main_tool
        
        try:
            selectedbones = context.selected_pose_bones
            cstmshap = selectedbones[0].custom_shape.name
            if cstmshap[:4] == 'Text':
                row = layout.row()
                row.label(text = 'Controller :')
                row = layout.row(align=True)
            
                if selectedbones[0].location == Vector((0,0,0)):
                    sign = 'PINNED'
                else:
                    sign = 'UNPINNED'
            
                row.operator('object.reset_bone', text='', icon = sign)
                row.separator()
                
                item = context.view_layer.objects.active.data.bones.active
                icon2 = 'OUTLINER_OB_FONT'
                if not item:
                    item = maintools
                    icon2 = 'BLANK1'
                    
                row.prop(item, "name", text="", icon = icon2)          
                row.operator('object.upd_cstmshp', text='', icon = 'FILE_PARENT')
                
                item = selectedbones[0]
                if item.name != item.custom_shape.data.body:
                    row = layout.row()
                    row.label(text = 'Update name of Custom Shape',icon='INFO')
                    
            
                row = layout.row()
                row.label(text = 'Scale:',icon='BLANK1')
                row.prop(item, 'custom_shape_scale', text='')
                row.label(text = '', icon='BLANK1')
                
                row = layout.row()
                row.label(text = 'Offset:', icon='BLANK1')
                text = bpy.data.curves[cstmshap]
                row.prop(text, "offset_x", text="")
                row.label(text = '', icon='BLANK1')
        except:
            pass
        
classes = [
            VIEW3D_PT_RigGenesis,
            VIEW3D_PT_Animation, 
            VIEW3D_PT_HelpButtons, 
            VIEW3D_PT_LipSync, 
            VIEW3D_PT_LipSync_Configuraton,
            AdjustBones, 
            SceneProperties,
            VIEW3D_MT_DeformationMode,
            ]
    
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    operators.register()
    WindowManager.adjust_mixam = PointerProperty(type=AdjustBones)
    bpy.types.Scene.archived = CollectionProperty(type = SceneProperties) 
    bpy.types.Scene.main_tool = PointerProperty(type=SceneProperties)
    WindowManager.bonefont_size = PointerProperty(type=SceneProperties)
    thumb_image()

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    operators.unregister()
    del WindowManager.adjust_mixam
    del WindowManager.bonefont_size
    del bpy.types.Scene.main_tool

    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
            
if __name__ == "__main__":
    register()