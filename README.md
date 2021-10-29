# SchedulePlanner
Schedule planner based on Lee algorithm.

### Usage

Install requirements.
```bash
python3 -m pip install -r requirements.txt
```

Run the server. Server will work on http://localhost:8000
```bash
cd backend
make local
```

Run client. Currently supported only CLI command.
```bash
# Use --help option to see full options
pyhton3 query_runner.py strategy1
```

### Tests
Run tests.
```bash
cd backend
python3 -m pip pytest -v
```

### Routes
```
GET    /hello            Basic get endpoint
POST   /api/strategy/1   Plan schedule by Strategy 1
                            - Require: {
                                field: [[int], [int], ...]
                                end_x: int
                              }
POST   /api/strategy/2   Plan schedule by Strategy 2
                            - Currently not implemented
POST   /api/strategy/3   Plan schedule by Strategy 3
                            - Currently not implemented
```
