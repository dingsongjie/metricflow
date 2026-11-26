# StarRocks support for MetricFlow (0.214.0)

This branch adds a StarRocks SQL engine to MetricFlow / dbt-metricflow, ported from
[dbt-labs/metricflow#2060](https://github.com/dbt-labs/metricflow/pull/2060) onto the
current `v0.214.0` codebase.

## Changes

| File | Change |
|------|--------|
| `metricflow/sql/render/starrocks.py` | New StarRocks SQL renderer (DATE_ADD/DATE_SUB, DAYOFWEEK→ISO DOW, DAYOFYEAR, PERCENTILE_APPROX, DATETIME) |
| `metricflow/protocols/sql_client.py` | `SqlEngine.STARROCKS` + unsupported granularities |
| `dbt-metricflow/dbt_metricflow/cli/dbt_connectors/adapter_backed_client.py` | register `starrocks` adapter type → engine + renderer |
| `dbt-metricflow/pyproject.toml` | `dbt-starrocks` extra |
| `dbt-metricflow/requirements-files/requirements-dbt-starrocks.txt` | `dbt-starrocks` |

## Usage

```bash
python -m pip install -e .
python -m pip install -e ./dbt-metricflow
python -m pip install "dbt-metricflow[dbt-starrocks]"
```

`profiles.yml`:

```yaml
my_project:
  target: starrocks
  outputs:
    starrocks:
      type: starrocks
      host: 127.0.0.1
      port: 9030
      username: root
      password: "..."
      schema: analytics
```

```bash
mf query --metrics my_metric --group-by metric_time --limit 10
```

## Status

- Live queries verified against StarRocks 4.x: simple, ratio, derived (cross-semantic-model), dimension joins.
- Official SQL snapshot suite for StarRocks is not wired into the test harness yet.

## License

Apache-2.0, same as upstream. See `LICENSE`.
