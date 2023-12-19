import pytest  
from src.uart import check_gpio_signal
import time

check_gpio_signal

def test_gpio_sgnal():  
    time.sleep(3)
    assert check_gpio_signal() == 'TEST-TX'

#def test_echo_single_byte():  
#    time.sleep(3)
#    assert echo_serial("1".encode()) == '1'  

#def test_echo_single_byte():  
#    time.sleep(3)
#    assert echo_serial("1".encode()) == '1'  

#def test_echo_multiple_bytes():  
#    with pytest.raises(TypeError):  
#        echo_serial(b'123')  

#def test_echo_number():  
#    with pytest.raises(TypeError):  
#        echo_serial(123)         
  
#def test_echo_string():  
#    with pytest.raises(TypeError):  
#        echo_serial("123")  
  
