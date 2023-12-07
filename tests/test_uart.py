import pytest  
from src.uart import echo_serial
  
def test_echo_single_byte():  
    assert echo_serial('1'.encode()) == '1'  

def test_echo_multiple_bytes():  
    with pytest.raises(TypeError):  
        echo_serial(b'123')  

def test_echo_number():  
    with pytest.raises(TypeError):  
        echo_serial(123)         
  
def test_echo_string():  
    with pytest.raises(TypeError):  
        echo_serial("123")  
  