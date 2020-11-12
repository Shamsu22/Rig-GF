   
import bpy
from var import (upd, ahj, bmp, cde, fv, ir, lth, quw, oy,
                smile, grin, sad, pout, angry, kiss,
                except_msg
)

from copy import deepcopy
from mixamo import disable_GNSrig
from utils import (
                    active_object, 
                    armature_name, 
                    figure_name, 
                    accessories, 
                    bone_zrotation,
                    mode_set,
                    select_all,
                    SUCCESS, 
                    INPUT_ERR, 
                    ERROR,
)
                                
kb = []
kb_names = []
ops = bpy.ops

def sorting_objects():
    figure_name.clear()
    armature_name.clear()
    armature = bpy.context.scene.main_tool.armatures
    mesh = bpy.context.scene.main_tool.meshes
    armature_name.append(armature)
    figure_name.append(mesh)
    objs = bpy.data.objects
    for obj in objs:
        if obj.parent and obj.type == "MESH":
            if (len(obj.data.vertices) > 500 
            and obj.parent.name == 
            objs[figure_name[0]].parent.name):
                accessories.append(obj.name)

def lip_bone_positioning(dict):
    for keys in dict.keys():
        values = dict[keys]
        if keys[1] == 'loc':
            move_pose_bone(keys[0], values)
        elif keys[1] == 'rot':
            rotation_pose_bone(keys[0], values)
        else:
            scale_pose_bone(keys[0], values)

def move_pose_bone(bone, val):
    pose_bones[bone].location = (val)
    
def rotation_pose_bone(bone, val):
    pose_bones[bone].rotation_quaternion = (val)    

def scale_pose_bone(bone, val):
    pose_bones[bone].scale = (val)
    
def purge_curves():
    for blocks in bpy.data.curves:
        if blocks.users == 0:
            bpy.data.curves.remove(blocks)
    for blocks in bpy.data.objects:
        if blocks.users == 0:
            bpy.data.objects.remove(blocks)

def empty_name_holders():     
    if armature_name:
        armature_name.clear()
    if figure_name:
        figure_name.clear()
    if accessories:
        accessories.clear()
            
def driver_scripted(drvr, tgtbname):
    var = drvr.driver.variables.new()
    var.type = 'SINGLE_PROP'
    target = var.targets[0]
    target.id = bpy.context.object
    targetbone = str([tgtbname])
    path =  "pose.bones"+targetbone+".custom_shape_scale"
    target.data_path = path.replace("'", '"')
    drvr.driver.expression = 'var'
    drvr.update()   
    
def create_lipsync_shapekeys(skname):
    mode_set('OBJECT')
    active_object(figure_name[0])
    obj = bpy.context.object
    try:
        listsk = list(obj.data.shape_keys.key_blocks)
        if listsk:
             shapekey = obj.shape_key_add(name=skname,from_mix=False)
    except AttributeError:
         shapekey = obj.shape_key_add(from_mix=False)
         shapekey = obj.shape_key_add(name=skname,from_mix=False)
    
def arma_create_lipsync_shapekeys(shapekey_name):
    mode_set('OBJECT')
    select_all('DESELECT')
    active_object(figure_name[0])
    obj = bpy.context.object
    ops.object.transform_apply(location=True,
                                rotation=True, 
                                scale=True)
    global modif
    for mod in bpy.context.object.modifiers:
        if mod.type == 'ARMATURE':
            modif =  mod.name
            
    if bpy.app.version >= (2, 90, 0):
        ops.object.modifier_apply_as_shapekey(
        modifier=modif)
    else:
        ops.object.modifier_apply(apply_as='SHAPE',
        modifier=modif)
        
    keyname = obj.data.shape_keys.name
    key = bpy.data.shape_keys[keyname]
    keyblock = key.key_blocks[modif]
    keyblock.name = shapekey_name
            
    active_object(armature_name[0])
    ops.object.transform_apply(location=True,
                                rotation=True,
                                scale=True)
    ops.object.parent_set(type='ARMATURE_NAME')
    mode_set('POSE')
    ops.pose.user_transforms_clear()
    
def duplicate_selected_text(name):
    ops.object.duplicate_move()
    ops.object.mode_set(mode='EDIT')
    ops.font.select_all()
    ops.font.text_insert(text = name)
    ops.object.mode_set(mode='OBJECT')

def shapekeys_drivers(drive, bonetrgt):
    drive.driver.type = 'AVERAGE'
    drive.driver.variables.new()
    variables = drive.driver.variables['var']
    variables.type = 'TRANSFORMS'
    targets = variables.targets[0]
    targets.id = bpy.data.objects[armature_name[0]]
    targets.bone_target = bonetrgt
    targets.transform_type = 'ROT_Z'
    targets.transform_space = 'LOCAL_SPACE'
    drive.modifiers.active.coefficients[1] = -0.3

def main_mesh():
    mesh_dict = {}
    objs = bpy.data.objects
    for obj in objs:
        if (obj.type == 'MESH'
        and obj.vertex_groups
        and obj.data.polygons
        and not obj.hide_viewport
        and not obj.users_collection[0].hide_viewport):
            mesh_dict[sum(obj.dimensions)] = obj.name
    max_dict = max(mesh_dict)
    mainmesh = mesh_dict[max_dict]
    return mainmesh

def scene_armatures(scene, context):
    items = []
    objs = context.scene.objects
    for obj in objs:
        if obj.type == 'ARMATURE':
            items.append((obj.name, obj.name, ""))
    return items

def scene_meshes(scene, context):
    items = []
    items.append((main_mesh(), main_mesh(), ""))
    objs = context.scene.objects
    for obj in objs:
        if (obj.type == 'MESH' 
        and obj.vertex_groups
        and obj.data.polygons
        and obj.name != main_mesh()):    
            items.append((obj.name, obj.name, ""))
    return items

def rename_textbones():
    items = []
    objs = bpy.context.scene.objects
    for obj in objs:
        if obj.type == 'FONT':
            items.append((obj.name, obj.name, ""))
    return items

def update_custom_shape():
    if not figure_name:
        sorting_objects()
    obj = bpy.context.object
    bone = obj.data.bones.active
    bonename = bone.name
    customshape = obj.pose.bones[bonename].custom_shape
    customshapebody = customshape.data.body
    if customshapebody == bonename:
        return
    customshape.data.body = bonename
    mode_set('OBJECT')
    select_all('DESELECT')
    active_object(figure_name[0])
    obj = bpy.context.object
    shape_keys = obj.data.shape_keys
    key_blocks = shape_keys.key_blocks
    key_blocks[customshapebody].name = bonename
    select_all('DESELECT')
    active_object(armature_name[0])
    mode_set('POSE')
    
def add_lip_ctrlr():
    if not figure_name:
        sorting_objects()
    #Getting highest bone
    mode_set('EDIT')
    select_all('DESELECT')
    obj = bpy.context.object
    editbones = obj.data.edit_bones
    figheight = [fh.figheightstore 
    for fh in bpy.context.scene.archived]
    for bone in editbones:
        bonelength = str(bone.length)
        extratedheight = str(figheight[0]/42)
        if bonelength[:5] == extratedheight[:5]:
            tailheight = {}
            tailheight[bone.tail[2]] = bone.name
            highesttail = max(tailheight) 
            highestbone = tailheight[highesttail]
    
    # Selecting highest bones and making a copy     
    mode_set('POSE')
    posebones = obj.pose.bones
    obj.data.bones.active = obj.data.bones[highestbone]
    posebone = posebones[highestbone]
    customshape = posebone.custom_shape
    customshapename = customshape.name
    mode_set('EDIT')
    editbone = editbones[highestbone]
    editbone.select = True
    for chld in editbone.children:
        chld.select = True
    
    mode_set('POSE')
    mode_set('EDIT')
    duplicate_move = ops.armature.duplicate_move
    duplicate_move(TRANSFORM_OT_translate={
                "value":(0, 0, figheight[0]/40)})
                
    #getting child and adding scale drivers
    mode_set('POSE') 
    obj.data.bones.active.name = 'New'       
    newbone = obj.data.bones.active
    newbonename = newbone.name 
    for ch in newbone.children:
        bname = ch.name
        bone = obj.pose.bones[bname]
        try:
            bone.driver_remove('custom_shape_scale')
        except:
            pass
        sdriver = bone.driver_add('custom_shape_scale')
        driver_scripted(sdriver, newbonename)
        if ch.name[:10] == 'Arrow_bone':
            driverbone = ch.name
    
    # Duplicating custom shape and storing
    mode_set('OBJECT')
    select_all('DESELECT')
    lscoll = bpy.data.collections['LS.Widget']
    lscoll.hide_viewport = False
    active_object(customshapename)
    bpy.ops.object.duplicate_move()
    obj = bpy.context.object
    newcustomshape = obj
    obj.data.body = newbonename
    select_all('DESELECT')
    # Creating Shapekey 
    active_object(figure_name[0])
    create_lipsync_shapekeys(newbonename)
    
    # Adding drivers
    mode_set('OBJECT')   
    select_all('DESELECT')
    active_object(figure_name[0])
    obj = bpy.context.object
    obj.show_only_shape_key = False
    obj.use_shape_key_edit_mode = False
    shape_keys = obj.data.shape_keys
    key_blocks = shape_keys.key_blocks
    driver = key_blocks[newbonename].driver_add('value')   
    shapekeys_drivers(driver, driverbone)
    select_all('DESELECT')
    lscoll.hide_viewport = True
    # Returning to pose mode
    active_object(armature_name[0])
    mode_set('POSE')
    posebones[newbonename].custom_shape = newcustomshape
    
def remove_lip_ctrlr():
    ops =  bpy.ops
    obj = bpy.context.object
    bone = obj.data.bones.active
    posebones = obj.pose.bones
    posebone = posebones[bone.name]
    customshapename = posebone.custom_shape.name
    bonename = posebone.name
    mode_set('EDIT')
    editbones = obj.data.edit_bones
    editbone = editbones[bone.name]
    editbone.select = True
    for chld in editbone.children:
        chld.select = True

    mode_set('POSE')
    mode_set('EDIT')
    bpy.ops.armature.delete()
    mode_set('OBJECT')
    select_all('DESELECT')
    lscoll = bpy.data.collections['LS.Widget']
    lscoll.hide_viewport = False
    active_object(customshapename)
    bpy.ops.object.delete()
    lscoll.hide_viewport = True
    purge_curves()
    if not armature_name:
        sorting_objects()
    bone_shapekey(figure_name[0], bonename)
    mode_set('OBJECT')
    ops.object.shape_key_remove(all=False)
    select_all('DESELECT')
    active_object(armature_name[0])
    mode_set('POSE')

def configure_lipsync(mode):
    sorting_objects()
    obj = bpy.context.object
    bone = obj.data.bones.active
    for ch in bone.children:
        if ch.name[:10] == 'Arrow_bone':
            driverbone = ch.name
            
    stuff = bpy.context.scene.archived[0]
    stuff.driverbonestore = driverbone
    bonename = bone.name
    select_all('SELECT')
    ops.pose.user_transforms_clear()
    obj.data.layers_protected[30] = True
    select_all('DESELECT')
    mode_set('OBJECT')
    bone_shapekey(figure_name[0], bonename)
    obj = bpy.context.object
    obj.use_shape_key_edit_mode = True
    key_blocks[bonename].name = '...' + kb_names[indx]
    if mode == 'POSE':
        mode_set('OBJECT')
        select_all('DESELECT')
        active_object(armature_name[0])
        mode_set(mode)
    elif mode == 'SCULPT':
        mode_set(mode)
    else:
        return
    
def bone_shapekey(activeobj, bonename):
    select_all('DESELECT')
    active_object(activeobj)
    obj = bpy.context.object
    shape_keys = obj.data.shape_keys
    global key_blocks
    key_blocks = shape_keys.key_blocks
    key_blocks[bonename].driver_remove('value')
    # Get index of shape key in bpy.context
    kb_names.clear()
    kb.clear()
    mode_set('EDIT')
    for k in key_blocks:
        kb_names.append(k.name)
    global indx
    indx = deepcopy(kb_names.index(bonename))
    keyname = obj.data.shape_keys.name
    bpy.data.shape_keys[keyname].key_blocks[bonename].value = 1
    obj.active_shape_key_index = indx
    
def apply_lipsync():
    mode_set('OBJECT')
    sorting_objects()
    obj = bpy.context.object
    select_all('DESELECT')
    if obj.type == 'MESH':
        apply_from_edit()
    else:
        apply_from_pose()

def apply_from_pose():
    active_object(figure_name[0])
    obj = bpy.context.object
    scene = bpy.context.scene
    maintool = scene.main_tool
    armaturename = maintool.armatures
    for mod in obj.modifiers:
        if (mod.type == 'ARMATURE' 
        and mod.object.name == armaturename):
            modifname =  deepcopy(mod.name)
            
    if bpy.app.version >= (2, 90, 0):
        ops.object.modifier_apply_as_shapekey(
        modifier=modifname)
    else:
        ops.object.modifier_apply(apply_as='SHAPE',
        modifier=modifname)
    keyname = obj.data.shape_keys.name
    key = bpy.data.shape_keys[keyname]
    existingshapekey = [sk for sk in key.key_blocks 
                    if sk.name[:3] == '...']
    newshapekey =  [sk for sk in key.key_blocks 
                    if sk.name == modifname]
    newshapekey[0].value = 1
    exshapekeyname = existingshapekey[0].name
    exshapekeyindx = obj.active_shape_key_index
    ops.object.shape_key_add(from_mix=True)
    mixshapekey = obj.active_shape_key
    shapekeylength = len(key.key_blocks)
    newshapekeyindx = shapekeylength - 2
    obj.active_shape_key_index = newshapekeyindx
    ops.object.shape_key_remove()
    obj.active_shape_key_index = exshapekeyindx
    ops.object.shape_key_remove()
    mixshapekey.name = exshapekeyname
    active_object(armature_name[0])
    ops.object.parent_set(type='ARMATURE_NAME')
    select_all('DESELECT')
    apply_from_edit()

def apply_from_edit():
    active_object(figure_name[0])
    obj = bpy.context.object
    obj.use_shape_key_edit_mode = False
    shape_keys = obj.data.shape_keys
    key_blocks = shape_keys.key_blocks
    kb_names.clear()
    kb.clear()
    for k in key_blocks:
        kb_names.append(k.name) 
        if k.name[:3] == '...':
            kb.append(k)
            
    kb[0].name = kb[0].name[3:]
    kb_name = kb[0].name
    driver = key_blocks[kb_name].driver_add('value')
    driverbone = [db.driverbonestore for db in 
                bpy.context.scene.archived]      
    shapekeys_drivers(driver, driverbone[0])
    select_all('DESELECT')
    active_object(armature_name[0])
    obj = bpy.context.object
    mode_set('POSE')
    select_all('SELECT')
    ops.pose.transforms_clear()
    select_all('DESELECT')
    obj.data.bones.active = obj.data.bones[kb_name]
    obj.data.bones.active.select = True
    bone_layers = range(32)
    for layer in bone_layers:
        obj.data.layers[layer] = False
        obj.data.layers[1] = True 

    obj.data.layers_protected[30] = False
    
def snap_cursor(type):
    area = bpy.context.area
    old_type = area.type
    area.type = 'VIEW_3D'
    if type == 'CENTER':
        ops.view3d.snap_cursor_to_center()
    elif type == 'SELECTED':
        ops.view3d.snap_cursor_to_selected()
    area.type = old_type
	
def create_lipsync():
    objs = bpy.data.objects 
    genesis = [obj.name for obj in objs 
            if obj.name[:7] == 'Genesis']
    rig = [obj.name for obj in objs 
            if obj.name == 'rig']
    gnsarma = [obj.name for obj in objs 
            if obj.name == 'GNSrig']
    scene = bpy.context.scene
    tool = scene.main_tool
    automodify = tool.auto_modify
    if not tool.armatures:
        return [ERROR, except_msg[14]] 
    if not tool.meshes:
        return [ERROR, except_msg[15]] 
    if automodify:
        if not genesis:
            return [ERROR, except_msg[16]] 
        elif not rig:
            return [ERROR, except_msg[17]]
        elif not gnsarma:
            return [ERROR, except_msg[18]]

    empty_name_holders()
    sorting_objects()
    scene = bpy.context.scene
    scene.transform_orientation_slots[0].type = 'GLOBAL'
    # Creating mesh of Bar custom shape
    snap_cursor('CENTER')
    ops.mesh.primitive_circle_add(
                                vertices=16, 
                                radius=0.25, 
                                enter_editmode=True)
    select_all('SELECT')
    ops.mesh.duplicate_move()
    ops.transform.resize(value=(0.9, 0.9, 0.9))
    select_all('DESELECT')
    mode_set('OBJECT')
    obj = bpy.context.object
    obj.name = 'Bar'
    me = obj.data
    for v1 in range(5,12):
        for v2 in range(21,28):
            me.vertices[v1].select = True
            me.vertices[v2].select = True
    mode_set('EDIT')
    ops.mesh.delete(type='VERT')
    select_all('SELECT')
    ops.mesh.edge_face_add()
    # Creating mesh for Arrow Custom Shape#
    #######################################
    mode_set('OBJECT')
    ops.mesh.primitive_plane_add(size=0.5, enter_editmode=True)
    ops.transform.resize(value=(0.1, 0.03, 1))
    select_all('DESELECT')
    mode_set('OBJECT')
    obj = bpy.context.object
    obj.name = 'Arrow'
    me = obj.data
    vert = [0,2]
    for v in vert:
        me.vertices[v].select = True
    mode_set('EDIT')
    ops.transform.translate(value=(-0.1, 0, 0))
    ops.mesh.extrude_region_move()
    ops.transform.resize(value=(1, 3, 1))
    ops.mesh.extrude_region_move(TRANSFORM_OT_translate={
                                    "value":(-0.075, 0, 0)})
    ops.mesh.merge(type='CENTER')
    select_all('DESELECT')
    mode_set('OBJECT')
    
     # Creating lip sync controller bones
    ####################################
    active_object(armature_name[0])
    objs = bpy.data.objects
    # Getting hieght of figure and bone
    global figheight
    figheight = objs[figure_name[0]].dimensions[2]
    if figheight > 2:
        pass
    else:
         figheight = 2  
    stuff = bpy.context.scene.archived.add()
    stuff.figheightstore = figheight
    mode_set('EDIT')
    arm =  bpy.context.object
    edit_bones = arm.data.edit_bones
    tailheight = {}
    for bone in edit_bones:
        tailheight[bone.tail[2]] = bone.name
        highesttail = max(tailheight)
    
    bone_layers = range(32)
    for layer in bone_layers:
        arm.data.layers[layer] = True 
        
    select_all('DESELECT')
    arrow_bone = edit_bones.new('Arrow_bone')        
    arrow_bone.select = True
    arrow_bone.length = 0.5
    bpy.ops.armature.select_more()

    # Manipulating bone scale and orientation
    arrow_bone.head[2] = highesttail
    arrow_bone.tail[2] = highesttail+1
    arrow_bone.length = figheight/20
    for layer in bone_layers:
        if layer == 1:
            arrow_bone.layers[layer] = True
        else:
            arrow_bone.layers[layer] = False
    
    ops.armature.calculate_roll(type='GLOBAL_NEG_Y')
    ops.transform.translate(value=(0.15, 0, -0.3))
    
    # Adding Text to serve as custom shape
    mode_set('OBJECT')
    ops.object.text_add()
    obj = bpy.context.object
    if bpy.app.version >= (2, 90, 0):
        ops.transform.rotate(value=-1.5708, orient_axis='X')
    else:
        ops.transform.rotate(value=1.5708, orient_axis='X')
        
    ops.transform.resize(value=(0.04, 0.04, 0.04))
    obj.display.show_shadows = False
    obj.hide_render = True
    obj.data.body = 'A-H-J'
    obj.data.fill_mode = 'NONE'  
    obj.data.offset_x = figheight/4
    # Creating Text customshape duplicates
    active_object('Text')
    duplicate_selected_text('B-M-P')
    duplicate_selected_text('C-D-E')
    duplicate_selected_text('F-V')
    duplicate_selected_text('I-R')
    duplicate_selected_text('L-Th') 
    duplicate_selected_text('Q-U-W')
    duplicate_selected_text('O-Y')
    #Creating bar bone
    active_object(armature_name[0])
    arm =  bpy.context.object
    mode_set('EDIT')
    ops.armature.duplicate_move()
    edit_bones['Arrow_bone.001'].name = "Bar_bone"
    mode_set('POSE')
    arm.pose.bones["Bar_bone"].custom_shape = bpy.data.objects["Bar"]
    mode_set('EDIT')
    #Creating text bone
    ops.armature.duplicate_move()
    edit_bones['Bar_bone.001'].name = "Text_bone"
    textbone = edit_bones['Text_bone']
    textbone.length  = figheight/42
    mode_set('POSE')
    
    #adding custom shape to bone
    arm =  bpy.context.object
    global pose_bones
    pose_bones = arm.pose.bones
    pose_arrow_bone = pose_bones["Arrow_bone"]
    pose_arrow_bone.custom_shape = bpy.data.objects["Arrow"]
    
    # Creating bone groups and assigning
    arm =  bpy.context.object
    pose_bones = arm.pose.bones
    barbone = pose_bones["Bar_bone"]
    pose_text_bone = arm.pose.bones["Text_bone"]
    lipctrl = arm.pose.bone_groups.new(name='Lips_ctrl')
    lipctrl.name = "lip_sync"
    lipctrl.color_set = 'THEME02'
    pointer_ctrl = arm.pose.bone_groups.new(name='pointer_ctrl')
    pointer_ctrl.name = "pointer_ctrl"
    pointer_ctrl.color_set = 'THEME09'
    barbone.bone_group = arm.pose.bone_groups['lip_sync']
    pose_text_bone.bone_group = arm.pose.bone_groups['lip_sync']
    pose_arrow_bone.bone_group = arm.pose.bone_groups['pointer_ctrl']
    
    # Limiting constraints
    limit_rot = pose_arrow_bone.constraints.new(type='LIMIT_ROTATION')
    limit_rot.use_limit_x = True
    limit_rot.use_limit_y = True
    limit_rot.use_limit_z = True
    limit_rot.min_z = -3.14159
    limit_rot.use_transform_limit = True
    limit_rot.owner_space = 'LOCAL'
    transform = pose_arrow_bone.constraints.new(type='TRANSFORM')
    transform.target = bpy.data.objects[armature_name[0]]
    transform.subtarget = "Text_bone"
    transform.use_motion_extrapolate = True
    transform.map_from = 'SCALE'
    transform.from_max_z_scale = 1.5
    transform.map_to = 'ROTATION'
    transform.to_max_z_rot = -3.14159
    transform.target_space = 'LOCAL'
    transform.owner_space = 'LOCAL'
    arm.data.bones["Arrow_bone"].use_deform = False
    ##############################################
    limit_scale = pose_text_bone.constraints.new(type='LIMIT_SCALE')
    limit_scale.use_min_x = True
    limit_scale.use_max_x = True
    limit_scale.use_min_y = True
    limit_scale.use_max_y = True
    limit_scale.use_min_z = True
    limit_scale.use_max_z = True
    limit_scale.owner_space = 'LOCAL'
    limit_scale.use_transform_limit = True
    limit_scale.min_x = 1
    limit_scale.max_x = 1
    limit_scale.min_y = 1
    limit_scale.max_y = 1
    limit_scale.min_z = 1
    limit_scale.max_z = 1.5
    limit_rot2 = pose_text_bone.constraints.new(type='LIMIT_ROTATION')
    limit_rot2.use_limit_x = True
    limit_rot2.use_limit_y = True
    limit_rot2.use_limit_z = True
    limit_rot2.owner_space = 'LOCAL'
        
    # Duplicating control bones
    mode_set('EDIT')
    new_bones= ('Arrow_bone', 'Bar_bone')
    for bones in new_bones:
        edit_bones[bones].parent = edit_bones['Text_bone']
        edit_bones[bones].select = True
        edit_bones[bones].hide_select = True 
    mode_set('POSE')
    mode_set('EDIT')
    times = 7
    while times:
        times -= 1
        duplicate_move = ops.armature.duplicate_move
        duplicate_move(TRANSFORM_OT_translate={"value":(0, 0, figheight/40)})
    
    # Adding custom bone and constraints targets
    mode_set('POSE')
    trg_bone = 'Text_bone'
    trg_bone2 = 'Arrow_bone'
    trg_obj = 'Text'
    flt =  0
    for bones in  pose_bones:
        while trg_bone == bones.name:
            pose_bones[trg_bone].custom_shape = bpy.data.objects[trg_obj]
            pose_bones[trg_bone2].constraints["Transformation"].subtarget = trg_bone
            flt += 0.001
            sflt = str(flt)
            if len(sflt) < 6:
                ext = sflt[1:]
            else:
                ext = sflt[1:5]
            trg_bone = trg_bone[:9] + ext
            trg_bone2 = trg_bone2[:10] + ext
            trg_obj = trg_obj[:4] + ext
            
    #Renaming Text bones              
    mode_set('EDIT')   
    lipsyncname = ['O-Y', 'Q-U-W', 'L-Th', 'I-R', 
                'F-V', 'C-D-E', 'B-M-P', 'A-H-J']
    shpkeyname = deepcopy(lipsyncname)
    lsbonename = deepcopy(lipsyncname)
    lsbname = deepcopy(lipsyncname)
    
    tbone = 'Text_bone'
    flt =  0       
    while lipsyncname:
        bname = lipsyncname[-1]
        edit_bones[tbone].name = bname
        flt += 0.001
        sflt = str(flt)
        if len(sflt) < 6:
            ext = sflt[1:]
        else:
            ext = sflt[1:5]
        tbone = tbone[:9] + ext
        lipsyncname.pop()
        
    # Moving pose bones
    ################################################
    mode_set('OBJECT')
    select_all('DESELECT')
    active_object(armature_name[0])
    arm =  bpy.context.object
    mode_set('POSE')
    select_all('SELECT')
    ops.pose.user_transforms_clear()
    
    #Create shapekeys
    scene = bpy.context.scene
    tool = scene.main_tool
    automodify = tool.auto_modify
    if automodify == True:
        lipbonecoord = [oy, quw, lth, ir, fv, cde, bmp, ahj]
        ahj.update(upd)  
        ir.update(upd)
        while shpkeyname:
            skname = shpkeyname[-1]
            lbname = lipbonecoord[-1]
            lip_bone_positioning(lbname)
            arma_create_lipsync_shapekeys(skname)
            shpkeyname.pop()             
            lipbonecoord.pop()
    else:
        while shpkeyname:
            skname = shpkeyname[-1]
            create_lipsync_shapekeys(skname)
            shpkeyname.pop()                   
    mode_set('OBJECT')
    # Adding drivers
    #####################################
    active_object(figure_name[0])
    obj = bpy.context.object
    obj.show_only_shape_key = False
    obj.use_shape_key_edit_mode = False
    shape_keys = obj.data.shape_keys
    key_blocks = shape_keys.key_blocks
    trg_bone2 = 'Arrow_bone'
    flt =  0
                
    while lsbonename:
        bname = lsbonename[-1]
        driver = key_blocks[bname].driver_add('value')
        shapekeys_drivers(driver, trg_bone2)
        flt += 0.001
        sflt = str(flt)
        if len(sflt) < 6:
            ext = sflt[1:]
        else:
            ext = sflt[1:5]
        trg_bone2 = trg_bone2[:10] + ext
        lsbonename.pop()
    
    select_all('DESELECT')
    active_object(armature_name[0])
    obj = bpy.context.object
    mode_set('POSE')
    trgbone = "Bar_bone"
    trgbone2 = "Arrow_bone"
    flt =  0
    
    while lsbname:
        bname = lsbname[-1]
        bone = obj.pose.bones[trgbone]
        sdriver = bone.driver_add('custom_shape_scale')
        driver_scripted(sdriver, bname)
        
        bone = obj.pose.bones[trgbone2]
        sdriver = bone.driver_add('custom_shape_scale')
        driver_scripted(sdriver, bname)
        flt += 0.001
        sflt = str(flt)
        if len(sflt) < 6:
            ext = sflt[1:]
        else:
            ext = sflt[1:5]
        trgbone = trgbone[:8] + ext
        trgbone2 = trgbone2[:10] + ext
        lsbname.pop()
    
    mode_set('OBJECT')    
    select_all('DESELECT')
    coll = bpy.data.collections.new('LS.Widget')
    if bpy.context.scene.collection.children:
        bpy.data.collections[0].children.link(coll)
    else:
        bpy.context.scene.collection.children.link(coll)
    coll.hide_viewport = True
    objs = bpy.data.objects
    for obj in objs:
        if obj.name == 'Bar' or obj.name =='Arrow' or obj.name[:4] == 'Text':
            obj.select_set(True)
            coll.objects.link(obj)
            ext_coll = obj.users_collection[0]
            ext_coll.objects.unlink(obj)   
    active_object(armature_name[0])
    mode_set('POSE')
    select_all('DESELECT')
    for layer in bone_layers:
        arm.data.layers[layer] = False
        arm.data.layers[1] = True 
        arm.data.layers_protected[30] = False
    return[SUCCESS]