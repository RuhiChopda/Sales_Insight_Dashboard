import pandas as pd
from pathlib import Path
import subprocess

def test_etl_creates_monthly_revenue(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    etl_script = repo_root / 'python_etl' / 'etl_to_sqlite.py'
    subprocess.check_call(['python', str(etl_script)])
    out_csv = repo_root / 'data' / 'monthly_revenue_for_powerbi.csv'
    assert out_csv.exists()
    df = pd.read_csv(out_csv)
    assert 'month' in df.columns
    assert df['revenue'].sum() > 0
