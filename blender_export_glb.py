import bpy
import os

# Caminho da pasta onde os objetos serão exportados
output_dir = "E:/URL_DE_EXEMPLO/Environment/"

# Certifique-se de que o diretório de saída existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Função para exportar um objeto como GLB
def export_glb(obj, filepath):
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the current object
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    # Export the selected object
    bpy.ops.export_scene.gltf(
        filepath=filepath,
        use_selection=True,
        export_format='GLB',  # Exporta como GLB
        export_yup=True  # Ajusta a orientação do eixo para Y para cima
    )

# Itera sobre todos os objetos no arquivo
for obj in bpy.data.objects:
    # Verifica se o objeto é do tipo 'MESH'
    if obj.type == 'MESH':
        # Construa o caminho de arquivo completo
        file_path = os.path.join(output_dir, obj.name + ".glb")
        # Exporta o objeto selecionado como .glb
        export_glb(obj, file_path)

print("Exportação concluída!")