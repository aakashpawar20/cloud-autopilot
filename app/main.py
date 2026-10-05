try:
    from fastapi import FastAPI
except ModuleNotFoundError:  # pragma: no cover - fallback for environments without FastAPI
    class FastAPI:
        def __init__(self, *args, **kwargs):
            pass

        def get(self, *args, **kwargs):
            def decorator(func):
                return func

            return decorator

app = FastAPI(
    title="Cloud Autopilot Demo Service",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "cloud-autopilot-demo",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.get("/metrics")
def metrics():
    return {
        "cpu_percent": 10,
        "memory_percent": 25,
        "error_rate": 0,
        "latency_ms": 50,
    }