def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_create_equipment(client):
    payload = {
        "name": "Notebook Dell",
        "responsible": "Pablo",
        "asset_tag": "PAT-001",
        "type": "Notebook",
        "status": "ativo"
    }

    response = client.post("/equipment", json=payload)

    assert response.status_code == 201

    data = response.get_json()

    assert data["message"] == "Equipamento cadastrado com sucesso."
    assert data["equipment"]["name"] == "Notebook Dell"

def test_get_equipment(client):
    payload = { 
        "name": "Notebook Dell",
        "responsible": "Jean",
        "asset_tag": "PAG_0100",
        "type": "Notebook",
        "status": "ativo"
    }

    create_response = client.post("/equipment", json=payload)

    assert create_response.status_code == 201

    data = create_response.get_json()

    assert data["message"] == "Equipamento cadastrado com sucesso."
    assert data["equipment"]["name"] == "Notebook Dell"

def  test_post_equipment(client):
    payload = { 
        "name": "tablet",
        "responsible": "marcos",
        "asset_tag": "PAG_0101",
        "status": "desativado",
        "type": "tablet",
    }

    cadastro_response = client.post('/equipment', json=payload)

    assert cadastro_response.status_code == 201

    data = cadastro_response.get_json()

    assert data["message"] == "Equipamento cadastrado com sucesso."
    assert data["equipment"]["name"] == "tablet"


def test_put_equipment(client):
    payload = {
        "name": "Notebook Dell",
        "responsible": "Pablo",
        "asset_tag": "PAT-010",
        "type": "Notebook",
        "status": "ativo",
    }

    create_response = client.post("/equipment", json=payload)

    assert create_response.status_code == 201

    equipment_id = create_response.get_json()["equipment"]["id"]

    update_payload = {
        "name": "Tablet",
        "responsible": "Marcos",
        "status": "desativado",
    }

    update_response = client.put(
        f"/equipment/{equipment_id}",
        json=update_payload
    )

    assert update_response.status_code == 200

    data = update_response.get_json()

    assert data["message"] == "Equipamento atualizado com sucesso."
    assert data["equipment"]["name"] == "Tablet"
    assert data["equipment"]["responsible"] == "Marcos"
    assert data["equipment"]["status"] == "desativado"

def test_delete_equipment(client):
    payload = {
        "name": "Notebook Dell",
        "responsible": "Pablo",
        "asset_tag": "PAT-010",
        "type": "Notebook",
        "status": "ativo",
    }

    create_response = client.post("/equipment", json=payload)

    assert create_response.status_code == 201

    equipment_id = create_response.get_json()["equipment"]["id"]

    delete_response = client.delete(
        f"/equipment/{equipment_id}"
    )

    assert delete_response.status_code == 200

    data = delete_response.get_json()

    assert data["message"] == "Equipamento Excluido com Sucesso"