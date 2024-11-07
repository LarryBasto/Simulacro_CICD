import subprocess

def test_hola():
    result = subprocess.run(['python', 'Hola.py'], capture_output=True, text=True)
    assert result.stdout.strip() == "Hola, Mundo"
