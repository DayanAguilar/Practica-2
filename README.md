# Instrucciones para Clonar el Repositorio y Ejecutar Pruebas

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/DayanAguilar/Practica-2.git
   cd Practica-2
   ```

2. **Instalar dependencias**:
   ```bash
   pip install pytest
   pip install coverage
   ```

3. **Ejecutar pruebas con pytest**:
   ```bash
   coverage run -m pytest
   ```

4. **Ejecutar pruebas con unittest**:
   ```bash
   coverage run -m unittest
   ```

5. **Generar reporte de cobertura**:
   ```bash
   coverage report -m
   ```

6. **Generar reporte en formato HTML**:
   ```bash
   coverage html
   ```

7. **Iniciar un servidor HTTP para ver el reporte HTML**:
   ```bash
   python3 -m http.server
   ```

De ahi podremos ver el reporte de covertura en formato html
