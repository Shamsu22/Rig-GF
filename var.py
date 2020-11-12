list_bones = [  # Value      # Name     # Description           
                ('head_bone', "Head", "Adjust Mixamo head bone", "BONE_DATA", 0),
                ('neck_bone', "Neck", "Adjust Mixamo neck bone", "BONE_DATA", 1),
                ('shoulder_bone', "Shoulder","Adjust Mixamo shoulder bone", "BONE_DATA", 2),
                ('uarm_bone', "Upper Arm", "Adjust Mixamo upper arm bone", "BONE_DATA", 3),
                ('larm_bone', "Lower Arm", "Adjust Mixamo lower arm bone", "BONE_DATA", 4),
                ('hand_bone', "Hand", "Adjust Mixamo hand bone", "BONE_DATA", 5),
                ('torso_bone', "Torso", "Adjust Mixamo torso bone", "BONE_DATA", 6),
                ('thigh_bone', "Thigh", "Adjust Mixamo Thigh bone", "BONE_DATA", 7),
                ('shin_bone', "Shin", "Adjust Mixamo Shin bone", "BONE_DATA", 8),
                ('foot_bone', "Foot", "Adjust Mixamo Foot bone", "BONE_DATA", 9),
                ('toe_bone', "Toe", "Adjust Mixamo Toe bone", "BONE_DATA", 10),
] 

fingerbones = ( 
                "ORG-f_index.01", "ORG-f_index.02", "ORG-f_index.03", "DEF-f_index.01", 
                "DEF-f_index.02", "DEF-f_index.03", "f_index.01_master", 
                "MCH-f_index.01_drv", "MCH-f_index.02_drv", "MCH-f_index.03_drv", 
                "MCH-f_index.03", "MCH-f_index.02", "MCH-f_index.01", "ORG-f_middle.01", 
                "ORG-f_middle.02", "ORG-f_middle.03", "DEF-f_middle.01", "DEF-f_middle.02", 
                "DEF-f_middle.03", "f_middle.01_master", "MCH-f_middle.01_drv", 
                "MCH-f_middle.02_drv", "MCH-f_middle.03_drv", "MCH-f_middle.03", 
                "MCH-f_middle.02", "MCH-f_middle.01", "ORG-f_ring.01", "ORG-f_ring.02", 
                "ORG-f_ring.03", "DEF-f_ring.01", "DEF-f_ring.02", "DEF-f_ring.03", 
                "f_ring.01_master", "MCH-f_ring.01_drv", "MCH-f_ring.02_drv", 
                "MCH-f_ring.03_drv", "MCH-f_ring.03", "MCH-f_ring.02", "MCH-f_ring.01", 
                "ORG-f_pinky.01", "ORG-f_pinky.02", "ORG-f_pinky.03", "DEF-f_pinky.01", 
                "DEF-f_pinky.02", "DEF-f_pinky.03", "f_pinky.01_master", 
                "MCH-f_pinky.01_drv", "MCH-f_pinky.02_drv", "MCH-f_pinky.03_drv", 
                "MCH-f_pinky.03", "MCH-f_pinky.02", "MCH-f_pinky.01",  "palm"
                )
                
face_controls = ('brow.B.L', 'brow.B.L.001', 'brow.B.L.002', 'brow.B.L.003', 'brow.B.L.004',
                'lid.B.L', 'lid.B.L.001', 'lid.B.L.002', 'lid.B.L.003', 'lid.T.L',
                'lid.T.L.001', 'lid.T.L.002', 'lid.T.L.003', 'brow.B.R', 'brow.B.R.001', 
                'brow.B.R.002', 'brow.B.R.003', 'brow.B.R.004', 'lid.B.R', 'lid.B.R.001', 
                'lid.B.R.002', 'lid.B.R.003', 'lid.T.R', 'lid.T.R.001', 'lid.T.R.002', 
                'lid.T.R.003', 'ear.L.002', 'ear.L.003', 'ear.L.004', 'ear.R.002', 
                'ear.R.003', 'ear.R.004', 'tongue', 'chin', 'chin.001', 'chin.L', 
                'chin.R', 'jaw', 'jaw.L.001', 'jaw.R.001', 'tongue.003', 'tongue.001', 
                'tongue.002', 'brow.T.L', 'brow.T.L.001', 'brow.T.L.002', 'brow.T.L.003', 
                'brow.T.R', 'brow.T.R.001', 'brow.T.R.002', 'brow.T.R.003', 'jaw.L', 'jaw.R', 
                'nose', 'nose.L', 'nose.R', 'lip.B', 'chin.002', 'lip.B.L.001', 'lip.B.R.001', 
                'cheek.B.L.001', 'cheek.B.R.001', 'lips.L', 'lips.R', 'lip.T.L.001', 
                'lip.T.R.001', 'lip.T', 'nose.005', 'nose.002', 'nose.001', 'nose.003', 
                'nose.004', 'nose.L.001', 'nose.R.001', 'cheek.T.L.001', 'cheek.T.R.001'
                )
toebones = ("SmallToe4", "SmallToe4_2", "SmallToe3", "SmallToe3_2", "SmallToe2", 
            "SmallToe2_2", "SmallToe1", "SmallToe1_2", "BigToe", "BigToe_2"
            )     
            
facialbones = ('CheekLower', 'NasolabialUpper', 'JawClench', 'LipUpperInner', 
                'LipUpperOuter', 'LipLowerInner', 'NasolabialLower', 'NasolabialMiddle', 
                'LipNasolabialCrease', 'Heel', 'SquintOuter', 'Eye', 'LipLowerOuter', 
                'LipCorner', 'SquintInner', 'Ear', 'LipBelowNose', 'Nostril', 'CheekUpper', 
                'NasolabialMouthCorner', 'BrowOuter', 'BrowInner', 'BrowMid'
                )
                
facialbones2 = ('lowerJaw', 'Nose', 'lowerFaceRig', 'LipLowerMiddle', 'LipBelow', 
                'Chin', 'BelowJaw', 'upperFaceRig', 'MidNoseBridge', 'LipUpperMiddle',
                'CenterBrow'
                )
FaceHeadParent = ("lowerJaw","upperFaceRig","Ear.L","Ear.R","upperTeeth","Eye.R","Eye.L",
            "LipCorner.L","LipCorner.R")
eyebones = ("EyelidInner", "EyelidLowerInner", "EyelidLower", "EyelidLowerOuter",
            "EyelidOuter", "EyelidUpperOuter", "EyelidUpper", "EyelidUpperInner"
            )   
browbones = ("brow.B.L", "brow.B.L.004", "brow.B.R", "brow.B.R.004")

adjust_bones = ('ThighBend.R','ThighTwist.R',
                'Shin.R','Shin.L','ForearmBend.L',
                'Hand.L', 'ShldrBend.L')

spine_target = [
                ('spine.007', 'head', 'chestUpper', 'head'),
                ('spine.008', 'head', 'chestLower', 'head')
                ]
                
deform_bones = ('upperFaceRig', 'lowerFaceRig', 'lowerJaw',
                'SmallToe4.L', 'SmallToe4_2.L', 'SmallToe3.L', 'SmallToe3_2.L', 
                'SmallToe2.L', 'SmallToe2_2.L', 'SmallToe1.L', 'SmallToe1_2.L', 
                'BigToe.L', 'BigToe_2.L', 'SmallToe4.R', 'SmallToe4_2.R', 
                'SmallToe3.R', 'SmallToe3_2.R', 'SmallToe2.R', 'SmallToe2_2.R', 
                'SmallToe1.R', 'SmallToe1_2.R', 'BigToe.R', 'BigToe_2.R')
                
hand_bones = ('ShldrBend.R','ShldrTwist.R','Hand.R','Thumb1.R','Thumb2.R','Thumb3.R',
            'Carpal1.R','Index1.R','Index2.R','Index3.R','Carpal2.R','Mid1.R','Mid2.R',
            'Mid3.R','Carpal3.R','Ring1.R','Ring2.R','Ring3.R','Carpal4.R','Pinky1.R',
            'Pinky2.R','Pinky3.R','ForearmBend.R','ForearmTwist.R', 'ThighBend.R','ThighTwist.R','Shin.R'
            )

arm1_bonepole_verts = [ #Bone--pole--G3M--G3F--G8F--G8M ||
                        ('head', 'tail', 78, 79, 79, 78),
                        ('lowerJaw', 'tail', 37, 37, 37, 37),
                        ('Eye.R', 'tail', 16211, 16866, 16211, 15902, 'yz'),
                        ('EyelidOuter.R', 'tail', 8761, 9234, 8879, 8407),
                        ('EyelidUpperOuter.R', 'tail', 7164, 7508, 7120, 6776),
                        ('EyelidUpper.R', 'tail', 7170, 7514, 7126, 6782), 
                        ('EyelidUpperInner.R', 'tail', 7343, 7687, 7296, 6952),
                        ('EyelidInner.R', 'tail', 8152, 8591, 8204, 7771), 
                        ('EyelidLowerInner.R', 'tail', 7232, 7576, 7188,6841), 
                        ('EyelidLower.R', 'tail', 7515, 7892, 7504, 7127), 
                        ('EyelidLowerOuter.R', 'tail', 7226, 7579, 7191, 6847),
                        ('Pectoral.R', 'tail', 17032, 13725, 12949, 14049),
                        ('Pectoral.R', 'head', 17032, 13725, 12949, 14049), 
                        ('Pectoral.R', 'head', 17025, 11379, 11002, 13858, 'yz'),
                        ('Shin.R', 'head', 7450, 7826, 928, 7062, 'yz')
                        ] 
arm2_bonepole_verts = [ #Bone--Pole--G3M--G3F--G8F--G8M
                        #Lips, chin, Jaw
                        ('lip.T.R', 'head', 20, 20, 19, 19), 
                        ('lip.T.R', 'tail', 7275, 7616, 7231, 6887), 
                        ('cheek.B.R', 'head', 7180, 9228, 7360,  6994), 
                        ('lip.T.R.001', 'tail', 7180, 9228, 7360,  6994), 
                        ('lip.T.R.001', 'tail', 7180, 9228, 7360,  6994), 
                        ('lip.B.R.001', 'tail', 7180, 9228, 7360,  6994), 
                        ('lip.B.R', 'head', 14, 14, 14, 14), 
                        ('lip.B.R', 'tail', 7188, 7532, 7144, 6800), 
                        ('chin.R', 'head', 8952, 8562, 8174, 8433), 
                        ('jaw', 'tail', 6518, 6846, 6458, 6130), 
                        ('chin', 'tail', 64, 64, 64, 64), 
                        ('chin.001', 'tail', 62, 62, 62, 62), 
                        ('jaw', 'head', 11, 11, 11, 11), 
                        #Nose
                        ('nose.001', 'tail', 60, 60, 60, 60), 
                        ('nose.R.001', 'tail', 60, 60, 60, 60), 
                        ('nose.002', 'tail', 66, 66, 66, 66), 
                        ('nose.003', 'tail', 67, 67, 67, 67), 
                        ('nose.R.001', 'head', 10243, 9282, 8894, 8419), 
                        ('nose.004', 'tail', 5315, 5619, 5255, 4951),
                        ('nose.R', 'head', 12919, 13546, 12770, 12144), 
                        ('nose', 'tail', 65, 65, 65, 65),
                        ('nose', 'head', 5292, 5596, 5232, 4928), 
                        #Cheek and Jaw
                        ('cheek.T.R.001', 'head', 9007, 9504, 9116, 8620), 
                        ('cheek.T.R', 'head', 12226, 12852, 12100, 11474),
                        ('cheek.B.R.001', 'tail', 12226, 12852, 12100, 11474), 
                        ('cheek.B.R.001', 'head', 12033, 12659, 11907, 11281), 
                        ('jaw.R.001', 'head', 8944, 9417, 9029, 8556), 
                        ('jaw.R', 'head', 12953, 13603, 12827, 12190),
                        #Ear and lids
                        ('ear.R.004', 'head', 12191, 12817, 12065, 11439), 
                        ('ear.R.004', 'tail', 13091, 13746, 12970, 12310), 
                        ('ear.R', 'head', 13091, 13746, 12970, 12310), 
                        ('ear.R', 'tail', 12179, 12805, 12053, 11428), 
                        ('ear.R.001', 'tail', 12173, 12799, 12047, 11431), 
                        ('ear.R.002', 'tail', 12996, 13646, 12870, 12220),  
                        ('lid.B.R.003', 'tail', 8761, 9234, 8879, 8407), 
                        #Brows
                        ('brow.B.R', 'head', 8936, 9402, 9014, 8548), 
                        ('brow.B.R.001', 'head', 8932, 9405, 9017, 8544), 
                        ('brow.B.R.002', 'head', 8927, 9400, 9012, 8539), 
                        ('brow.B.R.003', 'head', 8926, 9397, 9009, 8536), 
                        ('brow.B.R.003', 'tail', 11853, 9325, 8937, 11101),
                        ('brow.T.R.003', 'tail', 5292, 5596, 5232, 4928),
                        #Forehead
                        ('forehead.R', 'head', 11062, 11664, 11276, 10674), 
                        ('forehead.R.001', 'head', 11065, 11667, 11279, 10677), 
                        ('forehead.R.002', 'head', 11060, 11670, 11282, 10680), 
                        ('temple.R', 'head', 11929, 12555, 11803, 11177),
                        ('pelvis.R', 'tail', 7461, 8830, 8259, 7926, 'xz'), 
                        ('shoulder.R', 'head', 9483, 8799, 8411, 9092), 
                        #teeth 
                        ('teeth.T', 'head', 5774, 6195, 5714,  5525), 
                        ('teeth.T', 'tail', 5774, 6195, 5714,  5525), 
                        ('teeth.T', 'tail', 6103, 6363, 6007, 5739, 'y'),
                        ('teeth.B', 'head', 6238, 6302, 5964, 5634), 
                        ('teeth.B', 'tail', 6238, 6302, 5964, 5634), 
                        ('teeth.B', 'tail', 6103, 6363, 6007, 5739, 'y'),
                        ('spine.006', 'tail', 78, 79, 79, 78), 
                        ('face', 'tail', 76, 77, 77, 76), 
                        ('heel.02.R', 'tail', 10416, 10966, 10577, 10028)
                        ]
fcurves_indexes = (409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 
                    659, 660, 661, 662, 663, 664, 665, 666, 667, 668,
)
bones_target_bones = [ #---Arm1---=-Bone_poles----Arm1-----Bone_poles
                        ('chestLower', 'tail', 'chestUpper', 'head'), 
                        ('neckLower', 'head', 'chestUpper', 'tail'),
                        ('abdomenLower', 'tail', 'abdomenUpper', 'head'), 
                        ('abdomenLower', 'head', 'pelvis', 'head'), 
                        ('hip', 'tail', 'pelvis', 'head', 'dual'),
                        ]
arm2_bones_target = [  #---Arm2---=-Bone_poles2----Arm1-----Bone_poles1
                        #arm
                        ('shoulder.R', 'tail', 'Collar.R', 'tail'), 
                        ('upper_arm.R', 'head', 'Collar.R', 'tail'),
                        ('upper_arm.R', 'tail', 'ForearmBend.R', 'head'),
                        ('forearm.R', 'tail', 'Hand.R', 'head'),
                        ('hand.R', 'tail', 'Mid1.R', 'head'),
                        #Palms
                        ('palm.01.R', 'tail', 'Index1.R', 'head'),
                        ('palm.01.R', 'head', 'Carpal1.R', 'head'),
                        ('palm.02.R', 'head', 'Carpal2.R', 'head'),
                        ('palm.02.R', 'tail', 'Mid1.R', 'head'),
                        ('palm.03.R', 'tail', 'Ring1.R', 'head'),
                        ('palm.03.R', 'head', 'Carpal3.R', 'head'),
                        ('palm.04.R', 'head', 'Carpal4.R', 'head'),
                        ('palm.04.R', 'tail', 'Pinky1.R', 'head'),
                        #fingers pinky
                        ('f_pinky.01.R', 'head', 'Pinky1.R', 'head'),
                        ('f_pinky.01.R', 'tail', 'Pinky1.R', 'tail'),
                        ('f_pinky.02.R', 'head', 'Pinky2.R', 'head'),
                        ('f_pinky.02.R', 'tail', 'Pinky2.R', 'tail'),
                        ('f_pinky.03.R', 'head', 'Pinky3.R', 'head'),
                        ('f_pinky.03.R', 'tail', 'Pinky3.R', 'tail'),
                        #fingers Ring
                        ('f_ring.01.R', 'head', 'Ring1.R', 'head'),
                        ('f_ring.01.R', 'tail', 'Ring1.R', 'tail'),
                        ('f_ring.02.R', 'head', 'Ring2.R', 'head'),
                        ('f_ring.02.R', 'tail', 'Ring2.R', 'tail'),
                        ('f_ring.03.R', 'head', 'Ring3.R', 'head'),
                        ('f_ring.03.R', 'tail', 'Ring3.R', 'tail'),
                        #fingers Mid
                        ('f_middle.01.R', 'head', 'Mid1.R', 'head'),
                        ('f_middle.01.R', 'tail', 'Mid1.R', 'tail'),
                        ('f_middle.02.R', 'head', 'Mid2.R', 'head'),
                        ('f_middle.02.R', 'tail', 'Mid2.R', 'tail'),
                        ('f_middle.03.R', 'head', 'Mid3.R', 'head'),
                        ('f_middle.03.R', 'tail', 'Mid3.R', 'tail'),
                        #fingers index
                        ('f_index.01.R', 'head', 'Index1.R', 'head'),
                        ('f_index.01.R', 'tail', 'Index1.R', 'tail'),
                        ('f_index.02.R', 'head', 'Index2.R', 'head'),
                        ('f_index.02.R', 'tail', 'Index2.R', 'tail'),
                        ('f_index.03.R', 'head', 'Index3.R', 'head'),
                        ('f_index.03.R', 'tail', 'Index3.R', 'tail'),
                        #fingers Index
                        ('thumb.01.R', 'head', 'Thumb1.R', 'head'),
                        ('thumb.01.R', 'tail', 'Thumb1.R', 'tail'),
                        ('thumb.02.R', 'head', 'Thumb2.R', 'head'),
                        ('thumb.02.R', 'tail', 'Thumb2.R', 'tail'),
                        ('thumb.03.R', 'head', 'Thumb3.R', 'head'),
                        ('thumb.03.R', 'tail', 'Thumb3.R', 'tail'),
                        #Spine bones
                        ('spine.006', 'tail', 'head', 'tail'),
                        ('spine.006', 'head', 'head', 'head'),
                        ('face', 'head', 'head', 'head'),
                        ('spine.005', 'tail', 'neckUpper', 'tail'),
                        ('spine.004', 'tail', 'neckLower', 'tail'),
                        ('spine.004', 'head', 'neckLower', 'head'),
                        ('spine.003', 'tail', 'chestUpper', 'tail'),
                        ('spine.003', 'head', 'abdomenUpper', 'head'),
                        ('spine.002', 'head', 'abdomenLower', 'head'),
                        ('spine.001', 'head', 'hip', 'head'),
                        ('spine', 'head', 'pelvis', 'tail'),
                        ('pelvis.R', 'head', 'pelvis', 'tail'),
                        #pectoral
                        ('breast.R', 'head', 'Pectoral.R', 'head'),
                        ('breast.R', 'tail', 'Pectoral.R', 'tail'),
                        #legs
                        ('thigh.R', 'head', 'ThighBend.R', 'head'),
                        ('shin.R', 'head', 'Shin.R', 'head'),
                        ('foot.R', 'head', 'Foot.R', 'head'),
                        ('foot.R', 'tail', 'Toe.R', 'head'),
                        ('toe.R', 'tail', 'SmallToe2_2.R', 'tail'),
                        ('heel.02.R', 'head', 'Foot.R', 'head'),
                         #Eyes
                        ('lid.T.R', 'head', 'EyelidOuter.R', 'tail'),
                        ('lid.T.R.001', 'head', 'EyelidUpperOuter.R', 'tail'),
                        ('lid.T.R.002', 'head', 'EyelidUpper.R', 'tail', ),
                        ('lid.T.R.003', 'head', 'EyelidUpperInner.R', 'tail'),
                        ('lid.B.R', 'head', 'EyelidInner.R', 'tail',),
                        ('lid.B.R.001', 'head', 'EyelidLowerInner.R', 'tail'),
                        ('lid.B.R.002', 'head', 'EyelidLower.R', 'tail'),
                        ('lid.B.R.003', 'head', 'EyelidLowerOuter.R', 'tail'),
                        ('eye.R', 'head', 'Eye.R', 'head'),
                        ('eye.R', 'tail', 'Eye.R', 'tail'),
                        ('brow.T.R.002', 'tail', 'BrowInner.R', 'head'),
                        ('forehead.R', 'tail', 'BrowInner.R', 'head'),
                        ('brow.T.R.001', 'tail', 'BrowMid.R', 'head'),
                        ('forehead.R.001', 'tail', 'BrowMid.R', 'head'),
                        ('brow.T.R.001', 'head', 'BrowOuter.R', 'head'),
                        ('forehead.R.002', 'tail', 'BrowOuter.R', 'head'),
                        #mouth togue and Jaw
                        ('cheek.B.R', 'head', 'LipCorner.R', 'head'),
                        ('lip.B.R.001', 'tail', 'LipCorner.R', 'head'),
                        ('lip.T.R.001', 'tail', 'LipCorner.R', 'head'),
                        ('tongue', 'head', 'tongue04', 'tail'),
                        ('tongue.001', 'head', 'tongue03', 'tail'),
                        ('tongue.002', 'head', 'tongue02', 'tail'),
                        ('tongue.002', 'tail', 'tongue01', 'head')
                        ]    
rename_rig = [
                    ('head', 'Head_Ctrl'), ('DEF-nose', 'CenterBrow'), ('DEF-spine.006', 'head'), 
                    ('DEF-spine.005', 'neckUpper'), ('DEF-spine.004', 'neckLower'),   
                    ('DEF-spine.007', 'chestUpper'), ('DEF-spine.008', 'chestLower'), 
                    ('DEF-spine.003', 'abdomenUpper'), ('DEF-spine.002', 'abdomenLower'), 
                    ('DEF-spine.001', 'hip'), ('DEF-spine', 'pelvis'), ('ORG-teeth.T', 'upperTeeth'),            
                    ('ORG-teeth.B', 'lowerTeeth'), ('DEF-breast.R', 'Pectoral.R'), 
                    ('DEF-breast.L', 'Pectoral.L'), ('DEF-tongue', 'tongue04'), ('DEF-tongue.001', 'tongue03'),             
                    ('DEF-tongue.002', 'tongue02'), ('DEF-jaw', 'DEF-jaw-Redundant'), ('tongue.003', 'tongue01'),
                    #Eyes and Brows
                    ('DEF-lid.T.R', 'EyelidOuter.R'), ('DEF-lid.T.R.001', 'EyelidUpperOuter.R'),            
                    ('DEF-lid.T.R.002', 'EyelidUpper.R'), ('DEF-lid.T.R.003', 'EyelidUpperInner.R'),            
                    ('DEF-lid.B.R', 'EyelidInner.R'), ('DEF-lid.B.R.001', 'EyelidLowerInner.R'),            
                    ('DEF-lid.B.R.002', 'EyelidLower.R'), ('DEF-lid.B.R.003', 'EyelidLowerOuter.R'),
                    ('DEF-brow.T.R.003', 'BrowInner.R'), ('DEF-brow.T.R.002', 'BrowMid.R'), 
                    ('DEF-brow.T.R.001', 'BrowOuter.R'), 
                    #arm
                    ('DEF-shoulder.R', 'Collar.R'), ('DEF-upper_arm.R', 'ShldrBend.R'),            
                    ('DEF-upper_arm.R.001', 'ShldrTwist.R'), ('DEF-forearm.R', 'ForearmBend.R'),            
                    ('DEF-forearm.R.001', 'ForearmTwist.R'), ('DEF-hand.R', 'Hand.R'),       
                    #Fingers
                    ('DEF-thumb.01.R', 'Thumb1.R'), ('DEF-thumb.02.R', 'Thumb2.R'),             
                    ('DEF-thumb.03.R', 'Thumb3.R'), ('DEF-palm.01.R', 'Carpal1.R'), 
                    ('DEF-f_index.01.R', 'Index1.R'), ('DEF-f_index.02.R', 'Index2.R'),
                    ('DEF-f_index.03.R', 'Index3.R'), ('DEF-palm.02.R', 'Carpal2.R'), 
                    ('DEF-f_middle.01.R', 'Mid1.R'), ('DEF-f_middle.02.R', 'Mid2.R'),
                    ('DEF-f_middle.03.R', 'Mid3.R'), ('DEF-palm.03.R', 'Carpal3.R'),
                    ('DEF-f_ring.01.R', 'Ring1.R'), ('DEF-f_ring.02.R', 'Ring2.R'), 
                    ('DEF-f_ring.03.R', 'Ring3.R'), ('DEF-palm.04.R', 'Carpal4.R'), 
                    ('DEF-f_pinky.01.R', 'Pinky1.R'), ('DEF-f_pinky.02.R', 'Pinky2.R'),
                    ('DEF-f_pinky.03.R', 'Pinky3.R'),  
                    #Leg
                    ('DEF-thigh.R', 'ThighBend.R'), ('DEF-thigh.R.001', 'ThighTwist.R'),            
                    ('DEF-shin.R', 'Shin.R'), ('DEF-foot.R', 'Foot.R'), ('DEF-toe.R', 'Toe.R'),  

                    #Eyes and Brows
                    ('DEF-lid.T.L', 'EyelidOuter.L'), ('DEF-lid.T.L.001', 'EyelidUpperOuter.L'),            
                    ('DEF-lid.T.L.002', 'EyelidUpper.L'), ('DEF-lid.T.L.003', 'EyelidUpperInner.L'),            
                    ('DEF-lid.B.L', 'EyelidInner.L'), ('DEF-lid.B.L.001', 'EyelidLowerInner.L'),            
                    ('DEF-lid.B.L.002', 'EyelidLower.L'), ('DEF-lid.B.L.003', 'EyelidLowerOuter.L'),
                    ('DEF-brow.T.L.003', 'BrowInner.L'), ('DEF-brow.T.L.002', 'BrowMid.L'), 
                    ('DEF-brow.T.L.001', 'BrowOuter.L'), 
                    #arm
                    ('DEF-shoulder.L', 'Collar.L'), ('DEF-upper_arm.L', 'ShldrBend.L'),            
                    ('DEF-upper_arm.L.001', 'ShldrTwist.L'), ('DEF-forearm.L', 'ForearmBend.L'),            
                    ('DEF-forearm.L.001', 'ForearmTwist.L'), ('DEF-hand.L', 'Hand.L'),       
                    #Fingers
                    ('DEF-thumb.01.L', 'Thumb1.L'), ('DEF-thumb.02.L', 'Thumb2.L'),             
                    ('DEF-thumb.03.L', 'Thumb3.L'), ('DEF-palm.01.L', 'Carpal1.L'), 
                    ('DEF-f_index.01.L', 'Index1.L'), ('DEF-f_index.02.L', 'Index2.L'),
                    ('DEF-f_index.03.L', 'Index3.L'), ('DEF-palm.02.L', 'Carpal2.L'), 
                    ('DEF-f_middle.01.L', 'Mid1.L'), ('DEF-f_middle.02.L', 'Mid2.L'),
                    ('DEF-f_middle.03.L', 'Mid3.L'), ('DEF-palm.03.L', 'Carpal3.L'),
                    ('DEF-f_ring.01.L', 'Ring1.L'), ('DEF-f_ring.02.L', 'Ring2.L'), 
                    ('DEF-f_ring.03.L', 'Ring3.L'), ('DEF-palm.04.L', 'Carpal4.L'), 
                    ('DEF-f_pinky.01.L', 'Pinky1.L'), ('DEF-f_pinky.02.L', 'Pinky2.L'),
                    ('DEF-f_pinky.03.L', 'Pinky3.L'), 
                    #Leg
                    ('DEF-thigh.L', 'ThighBend.L'), ('DEF-thigh.L.001', 'ThighTwist.L'),            
                    ('DEF-shin.L', 'Shin.L'), ('DEF-foot.L', 'Foot.L'), ('DEF-toe.L', 'Toe.L')
                    ]
                    
bones_influence = [  #Bone--------------Constraints------Value
                    ("MCH-jaw_master.001", "Copy Transforms", 1),
                    ("MCH-jaw_master.002", "Copy Transforms", .75),
                    ("MCH-lid.T.R.002", "Damped Track", .65),
                    ("MCH-lid.T.L.002", "Damped Track", .65),
                    ("MCH-lid.T.R.001", "Damped Track", .80),
                    ("MCH-lid.T.L.001", "Damped Track", .80),
                    ("MCH-lid.B.R.002", "Damped Track", .75),
                    ("MCH-lid.B.L.002", "Damped Track", .75),
                    ]

custom_objs = [
            ("Pectoral", "WGT-rig_breast.L", 2, ""),
            ("Collar", "WGT-rig_shoulder.L", 1, ""),
            ("ShldrBend", "WGT-rig_upper_arm_fk.L", 2, ""),
            ("ForearmBend", "WGT-rig_upper_arm_fk.L", 2, ""),
            ("Hand", "WGT-rig_hand_fk.L", 5, ""),
            ("ThighBend", "WGT-rig_upper_arm_fk.L", 2, ""),
            ("Shin", "WGT-rig_upper_arm_fk.L", 1, ""),
            ("Foot", "WGT-rig_foot_fk.L", 20, ""),
            ("Toe", "WGT-rig_foot_fk.L", 6, ""),
            ("Thumb1", "WGT-rig_f_ring.01.L", 1,""),
            ("Thumb2", "WGT-rig_f_ring.01.L", 1.5,""), 
            ("Thumb3", "WGT-rig_f_ring.01.L", 1.5,""),
            ("Index1", "WGT-rig_f_ring.01.L", 1,""), 
            ("Index2", "WGT-rig_f_ring.01.L", 1.5,""), 
            ("Index3", "WGT-rig_f_ring.01.L", 1.5,""), 
            ("Mid1", "WGT-rig_f_ring.01.L", 1,""), 
            ("Mid2", "WGT-rig_f_ring.01.L", 1.5,""), 
            ("Mid3", "WGT-rig_f_ring.01.L", 1.5,""), 
            ("Ring1", "WGT-rig_f_ring.01.L", 1,""), 
            ("Ring2", "WGT-rig_f_ring.01.L", 1.5,""), 
            ("Ring3", "WGT-rig_f_ring.01.L", 1.5,""), 
            ("Pinky1", "WGT-rig_f_ring.01.L", 1,""), 
            ("Pinky2", "WGT-rig_f_ring.01.L", 1.5,""), 
            ("Pinky3", "WGT-rig_f_ring.01.L", 1.5,""),
            ("head", "WGT-rig_head", 1.2),
            ("neckUpper", "WGT-rig_neck", 1.2),
            ("neckLower", "WGT-rig_neck", 1),
            ("chestUpper", "WGT-rig_spine_fk.007", 1.5),
            ("chestLower", "WGT-rig_spine_fk.008", 1.5),
            ("abdomenUpper", "WGT-rig_spine_fk.003", 2),
            ("abdomenLower", "WGT-rig_spine_fk.002", 2),
            ("pelvis", "WGT-rig_spine_fk", 1),
            ("hip", "WGT-rig_torso", 15),
            ("MCH_eyeTarget", 'WGT-rig_eyes', 1)
]
                    
mixamo_bones = [#Bone----Contraint target
                ("head", "Head", "", ""), ("neckLower", "Neck", "neck", ""),
                ("chestLower", "Spine2", "chest", ""), ("abdomenUpper", "Spine1", "abdomen2", ""),
                ("abdomenLower", "Spine", "abdomen", ""), ("hip", "Hips", "", ""),
                #Arm
                ("Collar", "Shoulder", ""), ("ShldrBend", "Arm", "Shldr"),
                ("ForearmBend", "ForeArm", "ForeArm"), ("Hand", "Hand", ""),
                #fingers
                ("Pinky1", "HandPinky1", ""), ("Pinky2", "HandPinky2", ""),
                ("Pinky3", "HandPinky3", ""), ("Ring1", "HandRing1", ""), 
                ("Ring2", "HandRing2", ""), ("Ring3", "HandRing3", ""),
                ("Mid1", "HandMiddle1", ""),("Mid2", "HandMiddle2", ""),
                ("Mid3", "HandMiddle3", ""),("Index1", "HandIndex1", ""),
                ("Index2", "HandIndex2", ""), ("Index3", "HandIndex3", ""),
                ("Thumb1", "HandThumb1", ""), ("Thumb2", "HandThumb2", ""),
                ("Thumb3", "HandThumb3", ""),
                #Legs
                ("ThighBend", "UpLeg", "Thigh"), ("Shin", "Leg", ""), ("Foot", "Foot", ""),
                ("Toe", "ToeBase", ""),#("toe", "Toe_End", ""),
                #others
                ("pelvis", ""), ("Pectoral.R", ""), ("Pectoral.L", "")
                ]

upd =   {
        ('teeth.B', 'loc'): [-9.341965395703866e-11, 0.00023315855651162565, 0.003061968367546797],
        ('lip.B.L.001', 'loc'): [0.00012026064359815791, -0.005984284449368715, -0.0016421981854364276],
        ('lip.B.R.001', 'loc'): [-0.00012026064359815791, -0.005984284449368715, -0.0016421981854364276],
        ('lip.T.L.001', 'loc'): [0.001535053364932537, 0.0005117814871482551, 3.234426912968047e-05],
        ('lip.T.R.001', 'loc'): [-0.001535053364932537, 0.0005117814871482551, 3.234426912968047e-05],
        ('lip.B', 'loc'): [-0.00012113925913581625, -0.011856181547045708, -0.0015321634709835052],
        ('lips.L', 'loc'): [4.096885677928874e-11, 0.00822746753692627, 1.227296708705694e-09],
        ('lips.R', 'loc'): [-4.096885677928874e-11, 0.00822746753692627, 1.227296708705694e-09],
        }
ahj =   {
        ('jaw_master', 'rot'): [0.9993125796318054, 0.037072379142045975, 2.1293175450409763e-05, 6.024051981512457e-05],
        }
bmp =   {
        ('lip.B.L.001', 'loc'): [0.000776741886511445, 0.003527125809341669, -0.0028360532596707344],
        ('lip.B.R.001', 'loc'): [-0.000776741886511445, 0.003527125809341669, -0.0028360532596707344],
        ('lips.L', 'loc'): [0.0025963333901017904, -1.442057410983022e-12, 6.128599488874897e-05],
        ('lips.R', 'loc'): [-0.0025963333901017904, -1.442057410983022e-12, 6.128599488874897e-05],
        ('lip.T', 'loc'): [-1.071800692642455e-08, -0.01406857743859291, -0.017873143777251244],
        ('lip.B', 'loc'): [-0.0010062585351988673, 0.012448359280824661, -0.012727111577987671],
        ('LipLowerOuter.L', 'loc'): [-8.35179108094053e-08, -0.00796366948634386, 5.1713286666199565e-05],
        ('LipLowerOuter.L', 'rot'): [0.972722589969635, -0.23197150230407715, 2.0811403373954818e-05, -2.524977026041597e-05],
        ('LipLowerInner.L', 'loc'): [-2.8864960199825873e-07, -0.0030005439184606075, 0.00017873225442599505],
        ('LipLowerInner.L', 'rot'): [0.9637651443481445, -0.26675260066986084, -1.5337064951381763e-10, 8.057307354647492e-08],
        ('LipLowerMiddle', 'loc'): [1.0337999987314328e-12, -0.0022200681269168854, -9.928179389717684e-10],
        ('LipLowerMiddle', 'rot'): [0.9621926546096802, -0.2723701596260071, 1.2742338185489643e-05, -1.1277120393060613e-05],
        ('LipLowerInner.R', 'loc'): [2.8864960199825873e-07, -0.0030005439184606075, 0.00017873225442599505],
        ('LipLowerInner.R', 'rot'): [0.9637650847434998, -0.26675257086753845, 1.5337160708117636e-10, -8.057306644104756e-08],
        ('LipLowerOuter.R', 'loc'): [8.35179108094053e-08, -0.00796366948634386, 5.1713286666199565e-05],
        ('LipLowerOuter.R', 'rot'): [0.9727226495742798, -0.23197153210639954, -2.081140519294422e-05, 2.5249775717384182e-05],
        ('LipUpperMiddle', 'rot'): [0.9830869436264038, 0.18313953280448914, 1.7542908315251737e-12, -1.6009575887210303e-08],
        ('LipUpperOuter.L', 'loc'): [7.663360918064299e-11, 6.811338298939873e-11, 0.0008766649989411235],
        ('LipUpperOuter.L', 'rot'): [0.9739301800727844, 0.22684821486473083, 2.2046461878311163e-12, -1.9830451947200345e-08],
        ('LipUpperInner.L', 'rot'): [0.79801344871521, 0.6026397347450256, -2.7077227571226103e-08, 1.2572155760892656e-08],
        ('LipUpperInner.R', 'rot'): [0.7980135083198547, 0.6026396751403809, 2.7077225794869264e-08, -1.2572153984535817e-08],
        ('LipUpperOuter.R', 'loc'): [-7.663360918064299e-11, 6.811338298939873e-11, 0.0008766649989411235],
        ('LipUpperOuter.R', 'rot'): [0.9739301204681396, 0.22684822976589203, -2.2046461878311163e-12, 1.9830453723557184e-08],
        ('jaw_master', 'rot'): [0.9991718530654907, 0.04068836197257042, 2.3370110284304246e-05, 6.611631397390738e-05],
        }
cde =   {
        ('teeth.T', 'loc'): [-4.9432839765994885e-11, 3.095977918476933e-10, 0.0017313961870968342],
        ('teeth.B', 'loc'): [-5.2808993289410466e-11, -5.159963567535897e-10, 0.001731396303512156],
        ('chin', 'loc'): [-2.66434069251531e-10, -0.00414806604385376, -0.004869471304118633],
        ('lip.B.L.001', 'loc'): [0.00035564618883654475, -0.005230160430073738, -0.004856462124735117],
        ('lip.B.R.001', 'loc'): [-0.00035564618883654475, -0.005230160430073738, -0.004856462124735117],
        ('lip.T.L.001', 'loc'): [0.0028547588735818863, 0.001082062372006476, 6.73865870339796e-05],
        ('lips.L', 'loc'): [0.0071975961327552795, 0.006312331184744835, 0.00016989954747259617],
        ('lip.T.R.001', 'loc'): [-0.0028547588735818863, 0.001082062372006476, 6.73865870339796e-05],
        ('lips.R', 'loc'): [-0.0071975961327552795, 0.006312331184744835, 0.00016989954747259617],
        ('lip.B', 'loc'): [-0.0005828124121762812, -0.013165595941245556, -0.007371383719146252],
        ('LipLowerInner.L', 'loc'): [0.0016281665302813053, 0.0021291410084813833, 7.464839857362904e-10],
        ('LipLowerMiddle', 'loc'): [-5.463476338007922e-10, 0.0035067813005298376, -0.0018021758878603578],
        ('LipLowerInner.R', 'loc'): [-0.0016281665302813053, 0.0021291410084813833, 7.464839857362904e-10],
        }
fv =    {
        ('lip.T', 'rot'): [0.9100878834724426, 0.41441574692726135, -5.13149800429602e-11, -1.1303330493817043e-10],
        ('lip.B.L.001', 'loc'): [0.0003449208161327988, 0.0020637076813727617, -0.004710003267973661],
        ('lip.B.R.001', 'loc'): [-0.0003449208161327988, 0.0020637076813727617, -0.004710003267973661],
        ('lips.L', 'loc'): [-0.0012996322475373745, 2.9149460623045798e-12, -3.067760917474516e-05],
        ('lips.R', 'loc'): [0.0012996322475373745, 2.9149460623045798e-12, -3.067760917474516e-05],
        ('lip.B', 'loc'): [-0.0007451336132362485, 0.002307293936610222, -0.009424418210983276],
        ('LipLowerOuter.R', 'loc'): [-4.921196783413961e-10, -0.0032563223503530025, 0.0016281683929264545],
        ('LipLowerOuter.L', 'loc'): [4.921196783413961e-10, -0.0032563223503530025, 0.0016281683929264545],
        ('LipLowerInner.L', 'loc'): [3.7590469625925493e-10, -0.0022280497942119837, 0.0012446845648810267],
        ('LipLowerInner.L', 'rot'): [0.9677320122718811, -0.25198161602020264, -1.1769511754078366e-10, 7.613112984472536e-08],
        ('LipLowerInner.L', 'scale'): [1.0, 0.6948439478874207, 1.0],
        ('LipLowerMiddle', 'loc'): [-1.8249807220982461e-10, -0.002487295540049672, -0.0006023285677656531],
        ('LipLowerMiddle', 'rot'): [0.9573397636413574, -0.28896471858024597, -1.363524154696094e-10, 8.730444989168973e-08],
        ('LipLowerMiddle', 'scale'): [1.0, 0.4464094638824463, 1.0],
        ('LipLowerInner.R', 'loc'): [-3.7590469625925493e-10, -0.0022280497942119837, 0.0012446845648810267],
        ('LipLowerInner.R', 'rot'): [0.9677320122718811, -0.25198161602020264, 1.1769511754078366e-10, -7.613112984472536e-08],
        ('LipLowerInner.R', 'scale'): [1.0, 0.6948439478874207, 1.0],
        }
ir =    {
        ('jaw_master', 'rot'): [0.9983490109443665, 0.05744077265262604, 3.2992142223520204e-05, 9.333798516308889e-05],
        }
lth =   {
        ('teeth.B', 'loc'): [-5.470654484973636e-11, -0.000740781775675714, 0.0017761000199243426],
        ('lip.B.L.001', 'loc'): [-3.2741809263825417e-11, -0.0029949394520372152, 6.693881005048752e-10],
        ('lip.B.R.001', 'loc'): [3.2741809263825417e-11, -0.0029949394520372152, 6.693881005048752e-10],
        ('lips.L', 'loc'): [0.001298162736929953, -1.3151629091323613e-11, 3.064303018618375e-05],
        ('lips.R', 'loc'): [-0.001298162736929953, -1.3151629091323613e-11, 3.064303018618375e-05],
        ('lip.B', 'loc'): [2.3646862246096134e-11, -0.005322532262653112, -5.238689482212067e-10],
        ('LipLowerInner.L', 'loc'): [7.682432823230556e-08, 0.0004303611349314451, -4.634138895198703e-05],
        ('LipLowerMiddle', 'loc'): [2.3047299180234404e-07, 0.0012910834047943354, -0.00013902416685596108],
        ('LipLowerInner.R', 'loc'): [-7.682432823230556e-08, 0.0004303611349314451, -4.634138895198703e-05],
        ('tongue_master', 'loc'): [0.0001661879796301946, 0.008489602245390415, -0.006618700921535492],
        ('tongue_master', 'rot'): [0.9926754236221313, -0.12069304287433624, -0.00013536354526877403, -0.005376660265028477],
        ('jaw_master', 'rot'): [0.9985620975494385, 0.053608085960149765, 3.079075395362452e-05, 8.71100855874829e-05],
        }
oy =    {
        ('teeth.T', 'loc'): [-5.338773867435975e-11, 3.34367339371866e-10, 0.001869917381554842],
        ('teeth.B', 'loc'): [-5.6826779393226445e-11, 0.0001665259915171191, 0.0018624879885464907],
        ('lip.B.L.001', 'loc'): [8.798109774943441e-06, 0.0013472933787852526, -0.00012014081585220993],
        ('lip.B.R.001', 'loc'): [-8.798109774943441e-06, 0.0013472933787852526, -0.00012014081585220993],
        ('lip.T.L.001', 'loc'): [-7.74233967604232e-07, -0.003679010085761547, 3.2798237953102216e-05],
        ('lips.L', 'loc'): [-0.013208522461354733, 0.00024105588090606034, 0.0032881652005016804],
        ('lip.T.R.001', 'loc'): [7.74233967604232e-07, -0.003679010085761547, 3.2798237953102216e-05],
        ('lips.R', 'loc'): [0.013208522461354733, 0.00024105588090606034, 0.0032881652005016804],
        ('lip.T', 'loc'): [-4.778169526709064e-10, -5.7894894780474715e-06, -0.0006492403335869312],
        ('lip.B', 'loc'): [0.0, 0.0, 0.0],
        ('LipCorner.L', 'loc'): [-5.639044231564583e-10, 0.00025975689641200006, -0.0018179237376898527],
        ('LipLowerOuter.L', 'loc'): [-3.4275609550604713e-07, -0.0023352925200015306, 0.00020879867952317],
        ('LipLowerInner.L', 'loc'): [3.691058623189747e-07, -0.0025148207787424326, 0.00022485031513497233],
        ('LipLowerInner.R', 'loc'): [-3.691058623189747e-07, -0.0025148207787424326, 0.00022485031513497233],
        ('LipLowerOuter.R', 'loc'): [3.4275609550604713e-07, -0.0023352925200015306, 0.00020879867952317],
        ('LipCorner.R', 'loc'): [5.639044231564583e-10, 0.00025975689641200006, -0.0018179237376898527],
        ('LipUpperOuter.L', 'loc'): [1.4377396495568462e-10, 1.2778900160270723e-10, 0.001644730567932129],
        ('LipUpperInner.L', 'loc'): [7.189221440384586e-11, 6.389924700478389e-11, 0.000822424772195518],
        ('LipUpperInner.R', 'loc'): [-7.189221440384586e-11, 6.389924700478389e-11, 0.000822424772195518],
        ('LipUpperOuter.R', 'loc'): [-1.4377396495568462e-10, 1.2778900160270723e-10, 0.001644730567932129],
        ('jaw_master', 'rot'): [0.9990062117576599, 0.04457199200987816, 2.5600753360777162e-05, 7.242691208375618e-05],
        }
quw =   {
        ('lip.B.L.001', 'loc'): [-0.00024148794182110578, -1.2766880885806131e-09, 0.0032975946087390184],
        ('lip.B.R.001', 'loc'): [0.00024148794182110578, -1.2766880885806131e-09, 0.0032975946087390184],
        ('lip.T.L.001', 'loc'): [-7.802619074936956e-05, -1.872084931520135e-09, 0.0033055038657039404],
        ('lips.L', 'loc'): [-0.008519780822098255, -1.6608905362147652e-09, 0.003262587357312441],
        ('lip.T.R.001', 'loc'): [7.802619074936956e-05, -1.872084931520135e-09, 0.0033055038657039404],
        ('lips.R', 'loc'): [0.008519780822098255, -1.6608905362147652e-09, 0.003262587357312441],
        ('lip.T', 'loc'): [5.674613667849826e-09, 0.005713219754397869, 0.007721419911831617],
        ('lip.B', 'loc'): [0.0006085883360356092, -0.005713226739317179, 0.007697396911680698],
        ('LipLowerOuter.L', 'loc'): [-9.993792460250006e-10, 1.9713348731187352e-09, -0.0033064261078834534],
        ('LipLowerInner.L', 'loc'): [-9.993792460250006e-10, 1.9713346510741303e-09, -0.0033064261078834534],
        ('LipLowerMiddle', 'loc'): [-1.00243913170317e-09, 0.006570818834006786, -0.0033064233139157295],
        ('LipLowerInner.R', 'loc'): [9.993792460250006e-10, 1.9713346510741303e-09, -0.0033064261078834534],
        ('LipLowerOuter.R', 'loc'): [9.993792460250006e-10, 1.9713348731187352e-09, -0.0033064261078834534],
        ('LipUpperMiddle', 'loc'): [-4.850644330645082e-10, 0.0033064251765608788, -0.005548714194446802],
        ('LipUpperOuter.L', 'loc'): [-2.3872217543670013e-14, 0.003306425642222166, 7.77764963544314e-10],
        ('LipUpperInner.L', 'loc'): [-2.3872217543670013e-14, 0.003306425642222166, 7.777645194551042e-10],
        ('LipUpperInner.R', 'loc'): [2.3872217543670013e-14, 0.003306425642222166, 7.777645194551042e-10],
        ('LipUpperOuter.R', 'loc'): [2.3872217543670013e-14, 0.003306425642222166, 7.77764963544314e-10],
        ('lip.T.L.001', 'scale'): [1.0, 0.7207892537117004, 1.0],
        ('lip.T.R.001', 'scale'): [1.0, 0.7207892537117004, 1.0],
        ('lip.T', 'scale'): [1.0, 1.4078296422958374, 1.0],
        ('lip.B', 'scale'): [1.0, 1.5687298774719238, 1.0000001192092896],
        }   
smile = {
        ('lip.B.L.001', 'loc'): [0.004316858481615782, -1.38559844153896e-10, 0.0003161299682687968],
        ('lip.B.R.001', 'loc'): [-0.004316858481615782, -1.38559844153896e-10, 0.0003161299682687968],
        ('lip.T.L.001', 'loc'): [0.0036781318485736847, 0.002380629535764456, 8.682283078087494e-05],
        ('lips.L', 'loc'): [0.014216290786862373, 0.014335728250443935, -0.007977306842803955],
        ('lip.T.R.001', 'loc'): [-0.0036781318485736847, 0.002380629535764456, 8.682283078087494e-05],
        ('lips.R', 'loc'): [-0.014216290786862373, 0.014335728250443935, -0.007977306842803955],
        ('lip.B', 'loc'): [4.8903069094219376e-11, 0.001983881462365389, 5.89221615943103e-10],
        ('LipCorner.L', 'loc'): [0.00901754479855299, -0.014951436780393124, 0.008310516364872456],
        ('LipCorner.R', 'loc'): [-0.00901754479855299, -0.014951436780393124, 0.008310516364872456],
        }
grin = {
        ('lip.B.L.001', 'loc'): [0.005029385443776846, -0.004136320203542709, -0.009413650259375572],
        ('lip.B.R.001', 'loc'): [-0.005029385443776846, -0.004136320203542709, -0.009413650259375572],
        ('lip.T.L.001', 'loc'): [0.0036781318485736847, 0.0049777221865952015, 8.6823376477696e-05],
        ('lips.L', 'loc'): [0.014456630684435368, 0.014335732907056808, -0.01815907098352909],
        ('lip.T.R.001', 'loc'): [-0.0036781318485736847, 0.0049777221865952015, 8.6823376477696e-05],
        ('lips.R', 'loc'): [-0.014456630684435368, 0.014335732907056808, -0.01815907098352909],
        ('lip.T', 'loc'): [-7.073422576830968e-12, 0.004051445983350277, 1.8111376842711024e-09],
        ('lip.B', 'loc'): [-0.0006230255821719766, -0.014064433053135872, -0.007879998534917831],
        ('LipCorner.L', 'loc'): [0.009017548523843288, -0.014951435849070549, 0.01849505864083767],
        ('LipCorner.R', 'loc'): [-0.009017548523843288, -0.014951435849070549, 0.01849505864083767],
        }
sad= {
        ('lips.L', 'loc'): [0.004270561505109072, -0.00649260962381959, -0.009764873422682285],
        ('lips.R', 'loc'): [-0.004270561505109072, -0.00649260962381959, -0.009764873422682285],
        ('LipCorner.L', 'loc'): [0.00403894018381834, 0.006492615677416325, 0.009862876497209072],
        ('LipCorner.R', 'loc'): [-0.00403894018381834, 0.006492615677416325, 0.009862876497209072],
        }
pout = {
        ('lip.B.L.001', 'loc'): [-0.002816132502630353, 0.0016555438051000237, 0.006452478468418121],
        ('lip.B.R.001', 'loc'): [0.002816132502630353, 0.0016555438051000237, 0.006452478468418121],
        ('lip.T.L.001', 'loc'): [-5.8901889133267105e-05, 0.0016555443871766329, 0.0024953223764896393],
        ('lips.L', 'loc'): [-0.004695503041148186, -0.004861719440668821, 0.01403252873569727],
        ('lip.T.R.001', 'loc'): [5.8901889133267105e-05, 0.0016555443871766329, 0.0024953223764896393],
        ('lips.R', 'loc'): [0.004695503041148186, -0.004861719440668821, 0.01403252873569727],
        ('lip.T', 'loc'): [8.63148486018872e-09, 0.0016555407783016562, 0.011728135868906975],
        ('lip.B', 'loc'): [0.0009450715151615441, 0.0016555455513298512, 0.011953220702707767],
        }

angry = {
        ('lip.B.R.001', 'loc'): [-0.0004148892476223409, 4.402295861183347e-09, -0.0056654480285942554],
        ('lip.T.L.001', 'loc'): [-1.9375949456001962e-10, 0.008127688430249691, 2.0656596433354935e-09],
        ('lips.L', 'loc'): [0.0005108361365273595, -0.0013463114155456424, -0.002624036045745015],
        ('lip.T.R.001', 'loc'): [-0.0016227064188569784, 0.014593048021197319, 3.8307993236230686e-05],
        ('lip.T', 'loc'): [-1.6247683753967124e-11, 0.00930619053542614, 4.160191746649389e-09],
        }

kiss = {
        ('lip.B.L.001', 'loc'): [-0.00024148794182110578, -1.2766880885806131e-09, 0.0032975946087390184],
        ('lip.B.R.001', 'loc'): [0.00024148794182110578, -1.2766880885806131e-09, 0.0032975946087390184],
        ('lip.T.L.001', 'loc'): [-7.802619074936956e-05, -1.872084931520135e-09, 0.0033055038657039404],
        ('lips.L', 'loc'): [-0.012364707887172699, -3.522618863271987e-09, 0.0069301798939704895],
        ('lip.T.R.001', 'loc'): [7.802619074936956e-05, -1.872084931520135e-09, 0.0033055038657039404],
        ('lips.R', 'loc'): [0.012364707887172699, -3.522618863271987e-09, 0.0069301798939704895],
        ('lip.T', 'loc'): [5.674613667849826e-09, 0.005713219754397869, 0.007721419911831617],
        ('lip.B', 'loc'): [0.0007744291215203702, 0.002673148410394788, 0.009794943034648895],
        ('LipCorner.L', 'loc'): [-0.0037573084700852633, -5.227947519337306e-10, -0.0037572828587144613],
        ('LipLowerOuter.L', 'loc'): [-9.993792460250006e-10, 1.9713348731187352e-09, -0.0033064261078834534],
        ('LipLowerInner.L', 'loc'): [-9.993792460250006e-10, 1.9713346510741303e-09, -0.0033064261078834534],
        ('LipLowerMiddle', 'loc'): [-1.0006894202163608e-09, 0.002813460538163781, -0.003306424943730235],
        ('LipLowerInner.R', 'loc'): [9.993792460250006e-10, 1.9713346510741303e-09, -0.0033064261078834534],
        ('LipLowerOuter.R', 'loc'): [9.993792460250006e-10, 1.9713348731187352e-09, -0.0033064261078834534],
        ('LipCorner.R', 'loc'): [0.0037573084700852633, -5.227947519337306e-10, -0.0037572828587144613],
        ('LipUpperMiddle', 'loc'): [-3.4055055997406214e-10, 0.0033064254093915224, -0.0038955199997872114],
        ('LipUpperOuter.L', 'loc'): [-2.3872217543670013e-14, 0.003306425642222166, 7.77764963544314e-10],
        ('LipUpperInner.L', 'loc'): [-2.3872217543670013e-14, 0.003306425642222166, 7.777645194551042e-10],
        ('LipUpperInner.R', 'loc'): [2.3872217543670013e-14, 0.003306425642222166, 7.777645194551042e-10],
        ('LipUpperOuter.R', 'loc'): [2.3872217543670013e-14, 0.003306425642222166, 7.77764963544314e-10],
        ('lip.T.L.001', 'scale'): [1.0, 0.7207892537117004, 1.0],
        ('lip.T.R.001', 'scale'): [1.0, 0.7207892537117004, 1.0],
        ('lip.T', 'scale'): [1.0, 1.2571935653686523, 1.0],
        ('lip.B', 'scale'): [1.0, 1.3504143953323364, 1.000000238418579],
        }

except_msg = [
(#0
"Rigify add-on is not installed. \n \
Please go to: Edit > Preferences > Add-ons, to install Rigify Add-on"), 
(#1
"Purge Scene: \n \
A different Genesis Armature is present in the scene.\n\
Please go to help and press the 'Purge' button. "),
(#2
"Cannot execute: \n\
Multiple Genesis armature found in scene.\n\
Please select either of these armature('%s') and \n\
press the 'Clear' button to remove UNSELECTED items" ),
(#3
"Cannot execute:\n \
Nothing was selected. Please select '%s' armature"),
(#4
"Cannot execute: \n \
Selected object '%s' is a '%s' and not the Genesis armature.\n \
Please select '%s' armature" ),
(#5
"Cannot execute: \n \
Selected object '%s' is not recognised. \n \
Please select '%s' armature"),
(#6
"Cannot execute:\n \
Nothing was selected. \n \
Please import Genesis figure (FBX file) into scene and try again."),
(#7
"Cannot execute:\n \
Selected object '%s' is a '%s' and not an 'ARMATURE'.\n \
Please import Genesis figure (FBX file) into scene and try again."),
(#8
"Cannot execute:\n \
Selected object '%s' is not recognised.\n \
Please import Genesis figure (FBX file) into scene and try again."),
(#9
"Cannot execute:\n \
Armature mesh not recognised \n \
The mesh parented to the armature is not '%s.Shape"),
(#10
"Cannot execute: \n \
Please complete rigging process and try again"),
(#11
"Cannot execute: \n \
Please import an animated armature into the scene and try again. \n \
\n \
Visit www.mixamo.com to get animation templates in FBX format or \n \
Import an animated Genesis figure from Daz Studio in FBX format."),
(#12
"Cannot execute: \n \
A different animated armature is currently in scene. \n \
Remove armature and try again."),
(#13 Redundant
"Cannot execute: \n \
Please disable GNSrig before binding."),
(#14
"Cannot execute: \n \
Armature not found in current scene\n \
Add an Armature and try again."),
(#15
"Cannot execute: \n \
Weighted figure not found in current scene\n \
Add a weighted figure and try again."),
(#16
"Cannot execute: \n \
'Auto Modify' can only be used with Genesis figure. \n \
Uncheck 'Auto Modify' to proceed with current figure."),
(#17
"Cannot execute: \n \
Please complete rigging process to use 'Auto Modify Lips'. \n \
Uncheck 'Auto Modify' to proceed with current figure."),
(#18
"Cannot execute: \n \
'Auto Modify' is compatible only with figures rigged with 'Rig-GNS.' \n \
Uncheck 'Auto Modify' to proceed with current figure."),
]