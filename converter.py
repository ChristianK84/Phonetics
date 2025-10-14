import csv
import json
from collections import defaultdict

def convert_txt_to_json(input_file, output_file='output.json'):
    categories = defaultdict(list)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # Verifica que la fila tenga exactamente 4 columnas
                if len(row) != 4:
                    print(f"Fila inválida, se espera 4 columnas: {row}")
                    continue
                
                category, spanish, english, phonetic = [field.strip() for field in row]
                # Maneja valores vacíos
                word = {
                    'spanish': spanish or '',
                    'english': english or '',
                    'phonetic': phonetic or ''
                }
                # Solo agrega si spanish y english no están vacíos
                if word['spanish'] and word['english']:
                    categories[category].append(word)
    
        categories_data = {}
        for category, words in categories.items():
            categories_data[category] = {
                'count': len(words),
                'words': words
            }
    
        # Generar JSON
        json_output = json.dumps(categories_data, indent=4, ensure_ascii=False)
        
        # Guardar en archivo
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(json_output)
        
        return json_output
    
    except FileNotFoundError:
        return f"Error: No se encontró el archivo '{input_file}'"
    except Exception as e:
        return f"Error al procesar el archivo: {str(e)}"

# Uso
if __name__ == "__main__":
    json_output = convert_txt_to_json('Diccionario.txt')
    print(json_output)