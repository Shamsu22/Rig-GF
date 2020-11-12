import bpy

def principled_BSDF(mat):
    try:
        materials = bpy.data.materials
        nodes = materials[mat].node_tree.nodes
        inputs = nodes["Principled BSDF"].inputs
        inputs[4].default_value = 0
        inputs[5].default_value = 0.05
        inputs[7].default_value = 0.6
    except:
        pass
    
def adjust_materials():
    alpha = []
    skin = ('Fac', 'Tor', 'Lip', 
            'Ear', 'Arm', 'Leg'
            )
    materials = bpy.data.materials
    sclera = materials['Sclera'].node_tree.nodes
    eye_image = sclera['Image Texture'].image.name
    for mat in materials:
        try:
            matlist = list (mat.node_tree.nodes)
        except:
            pass
        for n in matlist:
            if n.type == 'BSDF_PRINCIPLED':
                principled_BSDF(mat.name)
            for i in n.inputs:
                if i.name == 'Alpha' \
                and i.is_linked == True:
                    mat.blend_method = 'HASHED'
                    mat.shadow_method = 'NONE'
            
        if (mat.name[:11] == 'EyeMoisture' 
        or mat.name[:6] == 'Cornea'):
            nodes = mat.node_tree.nodes
            nodes.clear()
            links = mat.node_tree.links
            sn = "ShaderNode"
            fresnel = nodes.new(sn+"Fresnel")
            fresnel.inputs['IOR'].default_value = 1.3
            fresnel.location= (-200, 400)
            trnspt = nodes.new(sn+"BsdfTransparent")
            trnspt.location = (-200,200)
            pbsdf = nodes.new(sn+"BsdfPrincipled")
            pbsdf.location = (-200,0)
            pbsdf.inputs['Metallic'].default_value = 1
            pbsdf.inputs['Specular'].default_value = 1
            pbsdf.inputs['Roughness'].default_value = 0
            pbsdf.inputs['Alpha'].default_value = 0.5
            mxshdr = nodes.new(sn+"MixShader")
            mxshdr.location = (200,200)
            mat_output = nodes.new(sn+"OutputMaterial")
            mat_output.location = (800,200)
            links.new(fresnel.outputs['Fac'], 
            mxshdr.inputs['Fac'])
            links.new(trnspt.outputs['BSDF'], 
            mxshdr.inputs[1])
            links.new(pbsdf.outputs['BSDF'], 
            mxshdr.inputs[2])
            links.new(mxshdr.outputs['Shader'],
            mat_output.inputs['Surface'])
            if mat.name[:6] == 'Cornea':
                tex_image = nodes.new(sn+"TexImage")
                tex_image.image = bpy.data.images[eye_image]
                tex_image.location = (-200, 800)
                diffuse = nodes.new(sn+"BsdfDiffuse")
                diffuse.location = (200,400)
                mxshdr2 = nodes.new(sn+"MixShader")
                mxshdr2.location = (600,200)

                links.new(tex_image.outputs['Color'], 
                diffuse.inputs['Color'])
                links.new(diffuse.outputs['BSDF'], 
                mxshdr2.inputs[1])
                links.new(mxshdr.outputs['Shader'], 
                mxshdr2.inputs[2])
                links.new(mxshdr2.outputs['Shader'], 
                mat_output.inputs['Surface'])
            mat.blend_method = 'BLEND'
            mat.shadow_method = 'NONE'
    for mat in materials:
        for s in skin:
            if mat.name[:3] == s:
                for nod in mat.node_tree.nodes:
                    if (nod.type == 'BSDF_PRINCIPLED' 
                    and nod.inputs[18].is_linked == True):
                        alpha.append(nod.inputs[18])
                for alp in alpha:
                    if nod.type == 'TEX_IMAGE' and \
                    nod.outputs['Color'].links[0].to_socket == alp:
                        mat.node_tree.nodes.remove(nod)
                        mat.blend_method = 'OPAQUE'
                        mat.shadow_method = 'OPAQUE'