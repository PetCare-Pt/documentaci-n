from datetime import datetime, timedelta
import math

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def get_next_workday(d):
    while d.weekday() >= 5:
        d += timedelta(days=1)
    return d

def count_workdays(start, end):
    count = 0
    d = start
    while d <= end:
        if d.weekday() < 5:
            count += 1
        d += timedelta(days=1)
    return count

def ms_dur(hours):
    mins = int(round(hours * 60))
    return "PT" + str(mins) + "M0S"

def fdt(d):
    return d.strftime("%Y-%m-%dT08:00:00")

def tag(indent, name, value):
    return indent + '<' + name + '>' + str(value) + '</' + name + '>'

# ─────────────────────────────────────────────
# TASK DATA
# ─────────────────────────────────────────────
ALL_TASKS = {
'Sprint 1': {
  'start': datetime(2026, 3, 16),
  'end':   datetime(2026, 3, 27),
  'label': '15 Mar - 29 Mar 2026',
  'groups': [
    ('PLAN','Actividades de planeacion del sprint',[
      ('T1','Sprint Planning S1 - Revision del Product Backlog y seleccion de items del sprint','Equipo',2,[]),
      ('T2','Sprint Planning S1 - Definicion del Sprint Goal y asignacion de tareas al equipo','Equipo',1,['T1']),
    ]),
    ('HU-01','Como usuario quiero registrarme en la plataforma',[
      ('T3','Crear proyecto Firebase, configurar acceso a la consola, y habilitar Firebase Authentication','Harold Ricardo Alvarado',5,['T2']),
      ('T4','Disenar prototipo de UI de formulario de registro','Andres Santiago Daza',4,['T2']),
      ('T7','Implementar formulario de registro y creacion de cuenta en Firebase Auth','Juan Jose Forero',7,['T3','T4','T5']),
      ('T8','Probar registro de usuarios','Anthony Alejandro Gonzalez',3,['T7','T6']),
    ]),
    ('HU-02','Como usuario quiero iniciar sesion con mi correo y contrasena',[
      ('T5','Disenar prototipo de UI de formulario de inicio de sesion','Juan Jose Forero',4,['T2']),
      ('T6','Disenar prototipo de UI de pagina de inicio','Anthony Alejandro Gonzalez',4,['T2']),
      ('T9','Implementar formulario de inicio de sesion y autenticacion con Firebase','Andres Santiago Daza',8,['T4','T5']),
      ('T10','Implementar pagina de inicio','Juan Jose Forero',7,['T7','T6','T9']),
      ('T11','Probar inicio de sesion y acceso a pagina de inicio','Anthony Alejandro Gonzalez',3,['T8','T10']),
    ]),
    ('HU-08','Como proveedor quiero crear y editar mi perfil profesional',[
      ('T12','Disenar modelado de datos de perfiles profesionales','Harold Ricardo Alvarado',5,['T3']),
      ('T13','Implementar DB perfiles profesionales','Harold Ricardo Alvarado',4,['T12']),
      ('T14','Disenar UI para formulario de creacion y edicion de perfil profesional','Juan Jose Forero',4,['T10']),
      ('T15','Implementar formulario de creacion y edicion de perfil profesional','Andres Santiago Daza',7,['T9','T14']),
      ('T16','Implementar endpoints de creacion y edicion de perfiles profesionales','Harold Ricardo Alvarado',10,['T13']),
      ('T17','Integrar llamadas a endpoints al crear/editar perfil profesional','Andres Santiago Daza',5,['T15','T16']),
      ('T18','Implementar despliegue de desarrollo para pruebas (HU-08)','Harold Ricardo Alvarado',6,['T16','T17']),
      ('T19','Ejecutar pruebas unitarias y de integracion (HU-08)','Anthony Alejandro Gonzalez',4,['T11','T18']),
    ]),
    ('HU-07','Como dueno de mascotas quiero crear y/o editar el perfil de mis mascotas',[
      ('T20','Disenar modelado de datos de perfiles de mascotas','Harold Ricardo Alvarado',5,['T18']),
      ('T21','Implementar modelos de datos en la DB (perfiles mascotas)','Harold Ricardo Alvarado',4,['T20']),
      ('T22','Disenar UI para formulario de creacion y edicion de perfil de mascota','Anthony Alejandro Gonzalez',4,['T19']),
      ('T23','Implementar formulario de creacion y edicion de perfil de mascota','Juan Jose Forero',7,['T14','T22']),
      ('T24','Implementar endpoints de creacion y edicion de perfiles de mascotas','Harold Ricardo Alvarado',10,['T21']),
      ('T25','Integrar llamadas a endpoints al crear/editar perfil de mascota','Juan Jose Forero',5,['T23','T24']),
      ('T26','Implementar despliegue de desarrollo para pruebas (HU-07)','Harold Ricardo Alvarado',6,['T24','T25']),
      ('T27','Ejecutar pruebas unitarias y de integracion (HU-07)','Andres Santiago Daza',4,['T17','T26']),
    ]),
    ('REUNIONES','Reuniones del sprint',[
      ('T28','Daily Standups Sprint 1 (15 reuniones de seguimiento diario)','Equipo',5,['T2']),
      ('T29','Sprint Review Sprint 1 - Demostracion del incremento a stakeholders','Equipo',2,['T8','T11','T19','T27','T28']),
      ('T30','Sprint Retrospective Sprint 1 - Analisis del proceso y propuesta de mejoras','Equipo',1.5,['T29']),
    ]),
    ('CIERRE','Actividades de cierre del sprint',[
      ('T31','Identificacion de lecciones aprendidas y cierre Sprint 1','Equipo',1,['T30']),
    ]),
  ]
},
'Sprint 2': {
  'start': datetime(2026, 3, 30),
  'end':   datetime(2026, 4, 10),
  'label': '29 Mar - 12 Abr 2026',
  'groups': [
    ('PLAN','Actividades de planeacion del sprint',[
      ('T32','Sprint Planning S2 - Revision del Product Backlog y seleccion de items del sprint','Equipo',2,[]),
      ('T33','Sprint Planning S2 - Definicion del Sprint Goal y asignacion de tareas al equipo','Equipo',1,['T32']),
    ]),
    ('HU-05','Como proveedor quiero publicar un nuevo servicio',[
      ('T34','Disenar modelado de datos de servicios e implementar coleccion en la DB','Harold Ricardo Alvarado',5,['T33']),
      ('T35','Disenar prototipo UI de formulario de creacion de servicio','Andres Santiago Daza',4,['T33']),
      ('T36','Implementar endpoints para la creacion de servicios','Harold Ricardo Alvarado',7,['T34']),
      ('T37','Implementar formulario de creacion de servicios con llamados a la API','Juan Jose Forero',7,['T35','T36','T40']),
      ('T38','Implementar despliegue de desarrollo para pruebas (HU-05)','Harold Ricardo Alvarado',4,['T36','T37']),
      ('T39','Ejecutar pruebas unitarias y de integracion (HU-05)','Anthony Alejandro Gonzalez',4,['T38']),
    ]),
    ('HU-04','Como usuario quiero ver el listado de servicios disponibles',[
      ('T40','Disenar prototipo de UI de pagina de visualizacion de servicios','Juan Jose Forero',5,['T33']),
      ('T41','Implementar endpoints para obtener listado de servicios y detalle','Harold Ricardo Alvarado',7,['T38']),
      ('T42','Implementar paginas para la visualizacion de servicios','Anthony Alejandro Gonzalez',9,['T39','T40','T41']),
      ('T43','Implementar despliegue de desarrollo para pruebas (HU-04)','Harold Ricardo Alvarado',4,['T41','T42']),
      ('T44','Ejecutar pruebas unitarias y de integracion (HU-04)','Juan Jose Forero',4,['T37','T43']),
    ]),
    ('HU-06','Como proveedor quiero gestionar la informacion de los servicios publicados',[
      ('T45','Disenar UI para la pagina de administracion de servicios','Andres Santiago Daza',5,['T35']),
      ('T46','Implementar endpoints para obtener informacion y editar servicios del proveedor','Harold Ricardo Alvarado',10,['T43']),
      ('T47','Implementar pagina de administracion de servicios con llamados a la API','Anthony Alejandro Gonzalez',10,['T42','T45','T46']),
      ('T48','Implementar despliegue de desarrollo para pruebas (HU-06)','Harold Ricardo Alvarado',4,['T46','T47']),
      ('T49','Ejecutar pruebas unitarias y de integracion (HU-06)','Juan Jose Forero',4,['T44','T48']),
    ]),
    ('HU-09','Como usuario quiero ver el perfil completo de cada proveedor',[
      ('T50','Disenar UI de la pagina de perfil profesional (publico)','Andres Santiago Daza',5,['T45']),
      ('T51','Implementar endpoints para obtener informacion del perfil profesional','Harold Ricardo Alvarado',7,['T48']),
      ('T52','Implementar pagina de perfil profesional con llamados a la API','Anthony Alejandro Gonzalez',8,['T47','T50','T51']),
      ('T53','Implementar despliegue de desarrollo para pruebas (HU-09)','Harold Ricardo Alvarado',4,['T51','T52']),
      ('T54','Ejecutar pruebas unitarias y de integracion (HU-09)','Andres Santiago Daza',4,['T50','T53']),
    ]),
    ('REUNIONES','Reuniones del sprint',[
      ('T55','Daily Standups Sprint 2 (15 reuniones de seguimiento diario)','Equipo',5,['T33']),
      ('T56','Sprint Review Sprint 2 - Demostracion del incremento a stakeholders','Equipo',2,['T39','T44','T49','T54','T55']),
      ('T57','Sprint Retrospective Sprint 2 - Analisis del proceso y propuesta de mejoras','Equipo',1.5,['T56']),
    ]),
    ('CIERRE','Actividades de cierre del sprint',[
      ('T58','Identificacion de lecciones aprendidas y cierre Sprint 2','Equipo',1,['T57']),
    ]),
  ]
},
'Sprint 3': {
  'start': datetime(2026, 4, 13),
  'end':   datetime(2026, 4, 24),
  'label': '12 Abr - 26 Abr 2026',
  'groups': [
    ('PLAN','Actividades de planeacion del sprint',[
      ('T59','Sprint Planning S3 - Revision del Product Backlog y seleccion de items del sprint','Equipo',2,[]),
      ('T60','Sprint Planning S3 - Definicion del Sprint Goal y asignacion de tareas al equipo','Equipo',1,['T59']),
    ]),
    ('HU-10','Como usuario quiero solicitar un servicio a un proveedor',[
      ('T61','Disenar modelado de datos de solicitudes e implementar coleccion en la DB','Harold Ricardo Alvarado',5,['T60']),
      ('T62','Disenar prototipo UI de paneles para clientes y proveedores','Andres Santiago Daza',4,['T60']),
      ('T63','Implementar endpoints para crear solicitud con pruebas y documentacion','Harold Ricardo Alvarado',7,['T61']),
      ('T64','Implementar Web Sockets para notificaciones de solicitudes','Harold Ricardo Alvarado',5,['T63']),
      ('T65','Implementar paneles y formulario de solicitud con llamados a la API','Juan Jose Forero',10,['T62','T63','T64','T68']),
      ('T66','Implementar despliegue de desarrollo para pruebas (HU-10)','Harold Ricardo Alvarado',4,['T64','T65']),
      ('T67','Ejecutar pruebas unitarias y de integracion (HU-10)','Anthony Alejandro Gonzalez',4,['T66']),
    ]),
    ('HU-11','Como proveedor quiero ver aceptar o rechazar solicitudes de servicio',[
      ('T68','Disenar prototipo de UI de componentes de gestion de solicitudes','Juan Jose Forero',5,['T60']),
      ('T69','Implementar endpoints para cambiar estado de solicitud y notificaciones','Harold Ricardo Alvarado',7,['T66']),
      ('T70','Implementar componentes de gestion de solicitudes con llamados a la API','Anthony Alejandro Gonzalez',9,['T67','T68','T69']),
      ('T71','Implementar despliegue de desarrollo para pruebas (HU-11)','Harold Ricardo Alvarado',4,['T69','T70']),
      ('T72','Ejecutar pruebas unitarias y de integracion (HU-11)','Juan Jose Forero',4,['T65','T71']),
    ]),
    ('HU-12','Como usuario quiero calificar y dejar una resena sobre el servicio',[
      ('T73','Disenar UI de formulario de resena','Andres Santiago Daza',5,['T62']),
      ('T74','Implementar endpoints para creacion de resenas con documentacion','Harold Ricardo Alvarado',7,['T71']),
      ('T75','Implementar formulario de creacion de resenas con llamados a la API','Anthony Alejandro Gonzalez',7,['T70','T73','T74']),
      ('T76','Implementar despliegue de desarrollo para pruebas (HU-12)','Harold Ricardo Alvarado',4,['T74','T75']),
      ('T77','Ejecutar pruebas unitarias y de integracion (HU-12)','Juan Jose Forero',4,['T72','T76']),
    ]),
    ('HU-14','Como proveedor quiero ver historial de servicios prestados y estadisticas',[
      ('T78','Disenar UI seccion de historial de servicios de proveedor','Andres Santiago Daza',5,['T73']),
      ('T79','Implementar endpoints para obtener estadisticas de servicios realizados','Harold Ricardo Alvarado',7,['T76']),
      ('T80','Implementar seccion de historial de servicios de proveedor','Anthony Alejandro Gonzalez',9,['T75','T78','T79']),
      ('T81','Implementar despliegue de desarrollo para pruebas (HU-14)','Harold Ricardo Alvarado',4,['T79','T80']),
      ('T82','Ejecutar pruebas unitarias y de integracion (HU-14)','Andres Santiago Daza',4,['T81']),
    ]),
    ('HU-13','Como usuario quiero ver historial completo de servicios solicitados',[
      ('T83','Disenar UI seccion de historial de servicios de cliente','Andres Santiago Daza',5,['T78','T82']),
      ('T84','Implementar endpoints para obtener estadisticas de servicios solicitados','Harold Ricardo Alvarado',7,['T81']),
      ('T85','Implementar seccion de historial de servicios de cliente con llamados a la API','Anthony Alejandro Gonzalez',9,['T80','T83','T84']),
      ('T86','Implementar despliegue de desarrollo para pruebas (HU-13)','Harold Ricardo Alvarado',4,['T84','T85']),
      ('T87','Ejecutar pruebas unitarias y de integracion (HU-13)','Andres Santiago Daza',4,['T83','T86']),
    ]),
    ('REUNIONES','Reuniones del sprint',[
      ('T88','Daily Standups Sprint 3 (15 reuniones de seguimiento diario)','Equipo',5,['T60']),
      ('T89','Sprint Review Sprint 3 - Demostracion del incremento a stakeholders','Equipo',2,['T67','T72','T77','T82','T87','T88']),
      ('T90','Sprint Retrospective Sprint 3 - Analisis del proceso y propuesta de mejoras','Equipo',1.5,['T89']),
    ]),
    ('CIERRE','Actividades de cierre del sprint',[
      ('T91','Identificacion de lecciones aprendidas y cierre Sprint 3','Equipo',1,['T90']),
    ]),
  ]
},
'Sprint 4': {
  'start': datetime(2026, 4, 27),
  'end':   datetime(2026, 5, 8),
  'label': '26 Abr - 10 May 2026',
  'groups': [
    ('PLAN','Actividades de planeacion del sprint',[
      ('T92','Sprint Planning S4 - Revision del Product Backlog y seleccion de items del sprint','Equipo',2,[]),
      ('T93','Sprint Planning S4 - Definicion del Sprint Goal y asignacion de tareas al equipo','Equipo',1,['T92']),
    ]),
    ('HU-15','Como administrador quiero ver dashboard con estadisticas generales de la plataforma',[
      ('T94','Disenar prototipo de UI de dashboard administrativo','Andres Santiago Daza',5,['T93']),
      ('T95','Implementar endpoints para obtener estadisticas de la plataforma','Harold Ricardo Alvarado',7,['T93']),
      ('T96','Implementar dashboard administrativo con llamados a la API','Juan Jose Forero',7,['T94','T95','T99']),
      ('T97','Implementar despliegue de desarrollo para pruebas (HU-15)','Harold Ricardo Alvarado',4,['T95','T96']),
      ('T98','Ejecutar pruebas unitarias y de integracion (HU-15)','Anthony Alejandro Gonzalez',4,['T97']),
    ]),
    ('HU-16','Como administrador quiero ver listado de usuarios y poder desactivar cuentas',[
      ('T99','Disenar prototipo de UI de panel de gestion de usuarios','Juan Jose Forero',5,['T93']),
      ('T100','Implementar panel de gestion de usuarios','Andres Santiago Daza',7,['T94','T99']),
      ('T101','Implementar obtencion de informacion de usuarios y acciones con Firebase','Anthony Alejandro Gonzalez',7,['T98','T100']),
      ('T102','Implementar despliegue de desarrollo para pruebas (HU-16)','Harold Ricardo Alvarado',4,['T97','T101']),
      ('T103','Ejecutar pruebas unitarias y de integracion (HU-16)','Juan Jose Forero',4,['T96','T102']),
    ]),
    ('HU-03','Como usuario quiero recibir correo de recuperacion de contrasena',[
      ('T104','Disenar UI para formulario de recuperacion de contrasena','Andres Santiago Daza',5,['T100']),
      ('T105','Implementar formulario de recuperacion de contrasena','Juan Jose Forero',7,['T103','T104']),
      ('T106','Configurar e implementar envio de correo de recuperacion con Firebase','Anthony Alejandro Gonzalez',7,['T101','T105']),
      ('T107','Implementar despliegue de desarrollo para pruebas (HU-03)','Harold Ricardo Alvarado',4,['T102','T106']),
      ('T108','Ejecutar pruebas unitarias y de integracion (HU-03)','Andres Santiago Daza',4,['T104','T107']),
    ]),
    ('REUNIONES','Reuniones del sprint',[
      ('T109','Daily Standups Sprint 4 (15 reuniones de seguimiento diario)','Equipo',5,['T93']),
      ('T110','Sprint Review Sprint 4 - Demostracion del incremento final a stakeholders','Equipo',2,['T98','T103','T108','T109']),
      ('T111','Sprint Retrospective Sprint 4 - Analisis final del proceso y lecciones aprendidas','Equipo',1.5,['T110']),
    ]),
    ('CIERRE','Actividades de cierre del sprint',[
      ('T112','Identificacion de lecciones aprendidas y cierre del proyecto','Equipo',1,['T111']),
    ]),
  ]
},
}

SPRINT_ORDER = ['Sprint 1','Sprint 2','Sprint 3','Sprint 4']

# ─────────────────────────────────────────────
# SCHEDULING
# ─────────────────────────────────────────────
def schedule_sprint(sprint_data):
    sprint_start = sprint_data['start']
    sprint_end   = sprint_data['end']
    registry = {}

    all_tasks_flat = []
    for (group_id, group_name, tasks) in sprint_data['groups']:
        for t in tasks:
            all_tasks_flat.append(t)

    for (tid, tname, owner, hours, preds) in all_tasks_flat:
        latest_pred_finish = None
        for pid in preds:
            if pid in registry:
                pf = registry[pid]['finish']
                if latest_pred_finish is None or pf > latest_pred_finish:
                    latest_pred_finish = pf

        if latest_pred_finish is None:
            task_start = get_next_workday(sprint_start)
        else:
            candidate = latest_pred_finish + timedelta(days=1)
            task_start = get_next_workday(candidate)
            if task_start > sprint_end:
                task_start = sprint_end

        wd = max(1, math.ceil(hours / 8))
        task_finish = task_start
        for _ in range(wd - 1):
            nxt = task_finish + timedelta(days=1)
            while nxt.weekday() >= 5:
                nxt += timedelta(days=1)
            task_finish = nxt

        if task_finish > sprint_end:
            task_finish = sprint_end
            avail_wd = count_workdays(task_start, sprint_end)
            hours = min(hours, avail_wd * 8)
            hours = max(hours, 1)

        registry[tid] = {'start': task_start, 'finish': task_finish, 'hours': hours}

    return registry

REGISTRIES = {name: schedule_sprint(ALL_TASKS[name]) for name in SPRINT_ORDER}

# ─────────────────────────────────────────────
# UID ASSIGNMENT & OWNER MAP
# ─────────────────────────────────────────────
UNIQUE_OWNERS = []
seen_owners = set()
for sname in SPRINT_ORDER:
    for (gid, gname, tasks) in ALL_TASKS[sname]['groups']:
        for (tid, tname, owner, hours, preds) in tasks:
            nm = owner.strip()
            if nm not in seen_owners:
                seen_owners.add(nm)
                UNIQUE_OWNERS.append(nm)

OWNER_UID = {name: (i+1) for i, name in enumerate(UNIQUE_OWNERS)}

uid_counter = [1]
def next_uid():
    v = uid_counter[0]
    uid_counter[0] += 1
    return v

PROJECT_UID = next_uid()
sprint_uids = {}
group_uids  = {}
task_uids   = {}

for sname in SPRINT_ORDER:
    sprint_uids[sname] = next_uid()
    for (gid, gname, tasks) in ALL_TASKS[sname]['groups']:
        group_uids[(sname, gid)] = next_uid()
        for (tid, tname, owner, hours, preds) in tasks:
            task_uids[tid] = next_uid()

# ─────────────────────────────────────────────
# XML GENERATION
# ─────────────────────────────────────────────
I1 = '  '
I2 = '    '
I3 = '      '
I4 = '        '

out = []
out.append('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
out.append('<Project xmlns="http://schemas.microsoft.com/project">')
out.append(tag(I1,'Name','PetCare MVP'))
out.append(tag(I1,'Title','PetCare MVP - Sprint Backlog'))
out.append(tag(I1,'StartDate','2026-03-16T08:00:00'))
out.append(tag(I1,'FinishDate','2026-05-08T17:00:00'))
out.append(tag(I1,'ScheduleFromStart','1'))
out.append(tag(I1,'DefaultDurationFormat','7'))
out.append(tag(I1,'DurationFormat','7'))
out.append(tag(I1,'HoursPerDay','8'))
out.append(tag(I1,'DaysPerMonth','20'))
out.append(tag(I1,'WeekStartDay','1'))
out.append(tag(I1,'CalendarUID','1'))

out.append(I1+'<Calendars>')
out.append(I2+'<Calendar>')
out.append(tag(I3,'UID','1'))
out.append(tag(I3,'Name','Standard'))
out.append(tag(I3,'IsBaseCalendar','1'))
out.append(I2+'</Calendar>')
out.append(I1+'</Calendars>')

out.append(I1+'<Tasks>')

row_id = [1]
def next_row():
    v = row_id[0]; row_id[0] += 1; return v

assignments = []
assign_id = [1]

def write_task_xml(uid, name, outline, is_summary, start_dt, finish_dt, hours,
                   pred_uids=None, notes=None):
    dur = ms_dur(hours)
    out.append(I2+'<Task>')
    out.append(tag(I3,'UID', uid))
    out.append(tag(I3,'ID',  next_row()))
    out.append(tag(I3,'Name', name))
    out.append(tag(I3,'OutlineLevel', outline))
    out.append(tag(I3,'Summary', '1' if is_summary else '0'))
    out.append(tag(I3,'Milestone','0'))
    out.append(tag(I3,'Start', fdt(start_dt)))
    out.append(tag(I3,'Finish', fdt(finish_dt)))
    out.append(tag(I3,'Duration', dur))
    out.append(tag(I3,'DurationFormat','7'))
    out.append(tag(I3,'Work', dur))
    out.append(tag(I3,'PercentComplete','0'))
    out.append(tag(I3,'CalendarUID','-1'))
    if notes:
        out.append(tag(I3,'Notes', notes))
    if pred_uids:
        for puid in pred_uids:
            out.append(I3+'<PredecessorLink>')
            out.append(tag(I4,'PredecessorUID', puid))
            out.append(tag(I4,'Type','1'))
            out.append(tag(I4,'CrossProject','0'))
            out.append(I3+'</PredecessorLink>')
    out.append(I2+'</Task>')

# Project summary
proj_start  = ALL_TASKS['Sprint 1']['start']
proj_finish = ALL_TASKS['Sprint 4']['end']
total_hours = sum(reg['hours'] for sn in SPRINT_ORDER for reg in REGISTRIES[sn].values())
write_task_xml(PROJECT_UID,'PetCare MVP',0,True,proj_start,proj_finish,total_hours)

for sname in SPRINT_ORDER:
    sdata = ALL_TASKS[sname]
    reg   = REGISTRIES[sname]
    s_uid = sprint_uids[sname]

    all_tids = [t[0] for (gid,gname,tasks) in sdata['groups'] for t in tasks]
    s_start  = min(reg[tid]['start']  for tid in all_tids)
    s_end    = max(reg[tid]['finish'] for tid in all_tids)
    s_hours  = sum(reg[tid]['hours']  for tid in all_tids)

    write_task_xml(s_uid, sname + ' (' + sdata['label'] + ')',
                   1, True, s_start, s_end, s_hours, notes=sdata['label'])

    for (gid, gname, tasks) in sdata['groups']:
        g_uid    = group_uids[(sname, gid)]
        g_tids   = [t[0] for t in tasks]
        g_start  = min(reg[tid]['start']  for tid in g_tids)
        g_end    = max(reg[tid]['finish'] for tid in g_tids)
        g_hours  = sum(reg[tid]['hours']  for tid in g_tids)

        write_task_xml(g_uid, gid + ' - ' + gname,
                       2, True, g_start, g_end, g_hours)

        for (tid, tname, owner, orig_hours, preds) in tasks:
            t_uid = task_uids[tid]
            t_reg = reg[tid]
            pred_uids_list = [task_uids[p] for p in preds if p in task_uids]

            write_task_xml(t_uid, '[' + tid + '] ' + tname,
                           3, False,
                           t_reg['start'], t_reg['finish'], t_reg['hours'],
                           pred_uids=pred_uids_list,
                           notes='Owner: ' + owner + ' | Hrs originales: ' + str(orig_hours))

            r_uid = OWNER_UID.get(owner.strip(), OWNER_UID['Equipo'])
            aid = assign_id[0]; assign_id[0] += 1
            assignments.append((aid, t_uid, r_uid, t_reg['hours']))

out.append(I1+'</Tasks>')

out.append(I1+'<Resources>')
for rname, ruid in OWNER_UID.items():
    out.append(I2+'<Resource>')
    out.append(tag(I3,'UID', ruid))
    out.append(tag(I3,'ID',  ruid))
    out.append(tag(I3,'Name', rname))
    out.append(tag(I3,'Type','1'))
    out.append(tag(I3,'MaxUnits','1'))
    out.append(tag(I3,'CalendarUID','1'))
    out.append(I2+'</Resource>')
out.append(I1+'</Resources>')

out.append(I1+'<Assignments>')
for (aid, tuid, ruid, hrs) in assignments:
    out.append(I2+'<Assignment>')
    out.append(tag(I3,'UID', aid))
    out.append(tag(I3,'TaskUID', tuid))
    out.append(tag(I3,'ResourceUID', ruid))
    out.append(tag(I3,'Work', ms_dur(hrs)))
    out.append(tag(I3,'Units','1'))
    out.append(I2+'</Assignment>')
out.append(I1+'</Assignments>')

out.append('</Project>')

xml_content = '\n'.join(out)

import os
out_dir = 'c:\\Users\\dazas\\Documents\\Universidad\\7 Semestre\\Gerencia\\documentaci\u00f3n\\startup'
os.makedirs(out_dir, exist_ok=True)

xml_path = out_dir + r'\PetCare_ProjectLibre.xml'
pod_path = out_dir + r'\PetCare_ProjectLibre.pod'

with open(xml_path, 'w', encoding='utf-8') as f:
    f.write(xml_content)
with open(pod_path, 'w', encoding='utf-8') as f:
    f.write(xml_content)

print("Generated:", xml_path)
print("Generated:", pod_path)
print("Total UIDs:", uid_counter[0]-1)
print("Total assignments:", len(assignments))

print("\n=== SCHEDULE SUMMARY ===")
for sname in SPRINT_ORDER:
    sdata = ALL_TASKS[sname]
    reg = REGISTRIES[sname]
    print(f"\n{sname} ({sdata['label']}):")
    print(f"  Window: {sdata['start'].strftime('%a %d %b')} -> {sdata['end'].strftime('%a %d %b')}")
    for (gid, gname, tasks) in sdata['groups']:
        for (tid, tname, owner, orig_h, preds) in tasks:
            r = reg[tid]
            adj = ' *ADJUSTED*' if abs(r['hours'] - orig_h) > 0.01 else ''
            print(f"  {tid}: {r['start'].strftime('%d/%m')} - {r['finish'].strftime('%d/%m')} "
                  f"({r['hours']:.1f}h orig={orig_h}h){adj}")
