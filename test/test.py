from src.main import *
from unittest.mock import patch

import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Lá vem o Chaves"}

@pytest.mark.asyncio
async def test_apresentar():
    result = await apresentar()
    assert result == {"Atividade Somativa 2 - DEVOPS"}

@pytest.mark.asyncio
async def test_numeroaleatorio():
    with patch('random.randint', return_value=2152):
        result = await numeroaleatorio()
    assert result == {"num_altr": 2152}

@pytest.mark.asyncio
async def test_create_colaborador():
    colaborador_teste = Colaborador(name="McLovin", setor="Financeiro", ativo=False)
    result = await create_colaborador(colaborador_teste)
    assert colaborador_teste == result

@pytest.mark.asyncio
async def test_update_colaborador_negativo():
    result = await update_colaborador(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_colaborador_positivo():
    result = await update_colaborador(10)
    assert result

@pytest.mark.asyncio
async def test_delete_colaborador_negativo():
    result = await delete_colaborador(-5)
    assert result

@pytest.mark.asyncio
async def test_delete_colaborador_positivo():
    result = await delete_colaborador(10)
    assert result