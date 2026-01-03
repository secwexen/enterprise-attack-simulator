from src.utils.config_loader import load_config
from src.utils.platform_detection import get_platform
from src.utils.logger import logger
import tempfile
import yaml


def test_config_loader_reads_yaml():
    """
    Ensures the config loader correctly reads YAML files.
    """
    sample_data = {"test_key": "test_value"}

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as tmp:
        yaml.dump(sample_data, tmp)
        tmp_path = tmp.name

    loaded = load_config(tmp_path)
    assert loaded == sample_data, "Config loader must return the same YAML content"


def test_platform_detection_returns_valid_string():
    """
    Ensures platform detection returns a valid platform identifier.
    """
    platform = get_platform()
    assert platform in ["windows", "linux", "macos", "unknown"]


def test_logger_outputs_without_error():
    """
    Ensures logger can write a simple log message without raising errors.
    """
    try:
        logger.info("Logger test message")
    except Exception as exc:
        assert False, f"Logger raised an unexpected exception: {exc}"
