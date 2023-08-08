def produccionAnual(codigo, P, PF):
    total_piezas = 0
    for i in range(len(P)):
        if P[i] == codigo:
            total_piezas += PF[i]
    return total_piezas


def rendimientoPromedio(codigo, P, PF, PD, CF, D):
    total_piezas_fabricadas = 0
    total_piezas_defectuosas = 0
    total_capacidad = 0
    total_dias_fabricacion = 0

    for i in range(len(P)):
        if P[i] == codigo:
            total_piezas_fabricadas += PF[i]
            total_piezas_defectuosas += PD[i]
            total_capacidad += CF[i]
            total_dias_fabricacion += 1

    rendimiento = (total_piezas_fabricadas -
                   total_piezas_defectuosas) / total_capacidad
    rendimiento_promedio_diario = rendimiento / total_dias_fabricacion
    return rendimiento_promedio_diario


def porcentajeAnualDefecto(codigo, P, PD, PF):
    total_piezas_fabricadas = 0
    total_piezas_defectuosas = 0

    for i in range(len(P)):
        if P[i] == codigo:
            total_piezas_fabricadas += PF[i]
            total_piezas_defectuosas += PD[i]

    porcentaje_defectos = (total_piezas_defectuosas /
                           total_piezas_fabricadas) * 100
    return porcentaje_defectos


def productosDefectuosos(codigos, P, PF, PD, porcentaje):
    productos_defectuosos = []
    for codigo in codigos:
        porcentaje_defectos = porcentajeAnualDefecto(codigo, P, PD, PF)
        if porcentaje_defectos > porcentaje:
            productos_defectuosos.append(codigo)
    return productos_defectuosos


def minimoPorcentajeDefecto(P, PF, PD):
    min_porcentaje_defecto = float('inf')
    min_codigo = ""

    for i in range(len(P)):
        porcentaje_defectos = (PD[i] / PF[i]) * 100
        if porcentaje_defectos < min_porcentaje_defecto:
            min_porcentaje_defecto = porcentaje_defectos
            min_codigo = P[i]

    return min_codigo


# Ejemplo de uso
P = ["ct-32", "mto-990", "ct-32"]
PF = [789, 1500, 900]
PD = [26, 35, 70]
D = [300, 12, 100]
CF = [1000, 2000, 1100]

# 1) Cantidad total de piezas "ct-32" fabricadas en el año
codigo = "ct-32"
total_piezas_anual = produccionAnual(codigo, P, PF)
print("Total de piezas 'ct-32' fabricadas en el año:", total_piezas_anual)

# 2) Rendimiento promedio diario para el código "mto-990"
codigo = "mto-990"
rendimiento_promedio = rendimientoPromedio(codigo, P, PF, PD, CF, D)
print("Rendimiento promedio diario para el código 'mto-990':", rendimiento_promedio)

#
