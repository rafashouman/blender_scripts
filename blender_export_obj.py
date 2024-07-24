import bpy
import os

# Caminho da pasta onde os objetos serão exportados
output_dir = "E:/URL_DE_EXEMPLO/Environment/"

# Certifique-se de que o diretório de saída existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Função para exportar um objeto como OBJ com Y para cima centralizados na posição x = 0 e y = 0, e z original
def export_obj(obj, filepath):
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the current object
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    # Salva a posição original do objeto
    original_location = obj.location.copy()

    # Move o objeto para a localização 0 nos eixos X e Y, mantendo a posição no eixo Z
    obj.location.x = 0
    obj.location.y = 0

    # Export the selected object
    bpy.ops.export_scene.obj(
        filepath=filepath,
        use_selection=True,
        axis_forward='-Z',  # Configura o eixo Z negativo para frente
        axis_up='Y',  # Configura o eixo Y para cima
        use_materials=True,  # Exporta com materiais
        keep_vertex_order=True,  # Mantém a ordem dos vértices
        path_mode='COPY'  # Copia as texturas para a pasta de destino
    )

    # Restaura a posição original do objeto
    obj.location = original_location

# Itera sobre todos os objetos no arquivo
for obj in bpy.data.objects:
    # Verifica se o objeto é do tipo 'MESH'
    if obj.type == 'MESH':
        # Construa o caminho de arquivo completo
        file_path = os.path.join(output_dir, obj.name + ".obj")
        # Exporta o objeto selecionado como .obj com Y para cima
        export_obj(obj, file_path)

print("Exportação concluída!")
