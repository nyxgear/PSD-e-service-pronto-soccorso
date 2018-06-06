# -*- coding: utf-8 -*-
from random import randint
import es_gestione_ambulanze.database as db


def stato_ambulanza(request_id):
    req = db.get(db.Richiesta, 'id', request_id)

    if req is None:
        return {'status': 'ERROR', 'type': 'NO REQUEST', 'message': 'Nessuna richiesta con questo id'}

    if not req.e_d['ambulanza_associata']:
        return {'status': 'ERROR', 'type': 'NO AMBULANZA', 'message': 'Nessuna ambulanza associata con questo id'}

    a = db.get(db.Ambulanza, 'id', req.e_d['ambulanza_id'])

    if not a:
        return {'status': 'ERROR', 'type': 'NOT FOUND',
                'message': 'Nessuna ambulanza trovata rispetto quella associata'}

    return {'result': a.to_dict(), 'status': 'SUCCESS'}


def nuova_richiesta_soccorso(es_PS_request):
    r_d = {
        'ambulanza_associata': False,
        'ambulanza_id': None,
        'es_PS_info': {'user': es_PS_request.get('user')}
    }

    # pick randomly whether to assign an ambulance

    if randint(0, 1):
        # if true, let's associate an ambulance
        r_d['ambulanza_associata'] = True
        r_d['ambulanza_id'] = 501

    new_request = db.Richiesta(r_d)
    db.save(new_request)

    print("NEW REQUEST")
    print(new_request.to_dict())

    return {
        'status': 'SUCCESS',
        'request_id': new_request.to_dict().get('id'),
        'ambulanza_associata': new_request.to_dict().get('ambulanza_associata')
    }
