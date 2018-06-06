# -*- coding: utf-8 -*-

import es_gestione_ambulanze.database as db


def stato_ambulanza(request_id):
    req = db.get(db.Richiesta, 'id', request_id)

    if req is None:
        return {'status': 'ERROR', 'type': 'NO REQUEST', 'message': 'Nessuna richiesta con questo id'}

    if not req.e_d['ambulanza_associata']:
        return {'status': 'ERROR', 'type': 'NO AMBULANZA', 'message': 'Nessuna ambulanza associata con questo id'}

    a = db.get(db.Ambulanza, 'id', req.e_d['ambulanza_id'])

    if not a:
        return {'status': 'ERROR', 'type': 'NOT FOUND', 'message': 'Nessuna ambulanza trovata rispetto quella associata'}

    return {'result': a.to_dict(), 'status': 'SUCCESS'}
