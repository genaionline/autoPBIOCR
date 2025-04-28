import pytest
from util.pbi_util import UtilPBI

# Test for connect_pbi method

def test_connect_pbi_valid_link(monkeypatch):
    def mock_get(section, option):
        return "http://valid-link-to-power-bi"
    
    monkeypatch.setattr('configparser.ConfigParser.get', mock_get)
    
    try:
        UtilPBI.connect_pbi()
        assert True
    except Exception:
        assert False, "connect_pbi() raised an exception unexpectedly!"


def test_connect_pbi_invalid_link(monkeypatch):
    def mock_get(section, option):
        return "<your_power_bi_link_here>"
    
    monkeypatch.setattr('configparser.ConfigParser.get', mock_get)
    
    with pytest.raises(ValueError, match="Invalid Power BI link."):
        UtilPBI.connect_pbi()

# Test for export_to_pdf method

def test_export_to_pdf():
    try:
        UtilPBI.export_to_pdf("output.pdf", {"filter_key": "filter_value"})
        assert True
    except Exception:
        assert False, "export_to_pdf() raised an exception unexpectedly!" 

