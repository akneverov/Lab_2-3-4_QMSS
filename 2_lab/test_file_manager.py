import pytest
import file_manager as fm

#Тест функции №1 просмотр всех файлов папки
@pytest.fixture()
def ls_fixture():
    fm.ls()
    return True
def test_ls(ls_fixture):
    assert ls_fixture == True

#Тест функции №2 создание пустых файлов с указанием имени;
@pytest.fixture()
def create_fixture():
    fm.create('ind.txt')
    return True
def test_create(create_fixture):
    assert create_fixture == True

#Тест функции №3  Дозапись текста в файл;
@pytest.fixture()
def add_fixture():
    fm.add('new.txt', ', privet snova')
    return True
def test_add(add_fixture):
    assert add_fixture == True

#Тест функции №4 Переименование файлов
@pytest.fixture()
def rename_fixture():
    fm.rename('ind.txt', 'new_ind.txt')
    return True
def test_rename(rename_fixture):
    assert rename_fixture == True

#Тест функции №5 Удаление файлов по имени
#(Негативное тестирование (проверка на ошибку))
@pytest.fixture()
def remove_fixture():
    try:
        fm.rmv('')
        return True
    except:
        return False
def test_remove(remove_fixture):
    assert remove_fixture == False

#Тест функции №6 Запись текста в файл;
@pytest.fixture()
def rewrite_fixture():
    fm.rewrite('new.txt', 'privet')
    return True
def test_rewrite(rewrite_fixture):
    assert rewrite_fixture == True

#Тест функции №7 Копирование файлов из одной папки в другую;
@pytest.fixture()
def copy_fixture():
    fm.copy('new_ind.txt', 'new_ind2.txt')
    return True
def test_copy(copy_fixture):
    assert copy_fixture == True

#Тест функции №8 Перемещение файлов;
@pytest.fixture()
def move_fixture():
    fm.move('new_ind2.txt', 'new_ind3.txt')
    return True
def test_move(move_fixture):
    assert move_fixture == True

#Тест функции №9 просмотр всех файлов папки
@pytest.fixture()
def ls_fixture():
    fm.ls()
    return True
def test_ls(ls_fixture):
    assert ls_fixture == True

#Тест функции №10 Создание папки;
@pytest.fixture()
def mkfold_fixture():
    fm.mkfold('newfold')
    return True
def test_mkfold(mkfold_fixture):
    assert mkfold_fixture == True

#Тест функции №11 Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
@pytest.fixture()
def cf_fixture():
    fm.cf('./newfold')
    return True
def test_cf(cf_fixture):
    assert cf_fixture == True

#Тест функции №12 Удаление папки;
@pytest.fixture()
def rmfold_fixture():
    fm.rmfold('newfold')
    return True
def test_rmfold(rmfold_fixture):
    assert rmfold_fixture == True