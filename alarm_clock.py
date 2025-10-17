from datetime import datetime, timedelta
import time

print("ALARM CLOCK -Etape 1(sans son)")

hhmm = input("Entrez l'heure (HH:MM) ex: 07:30 > ").strip()

def parse_time_str(hhmm: str) -> datetime:
    now = datetime.now()
    try:
        hour, minute =map(int, hhmm.split(":"))
    except Exception:
        raise ValueError("Format invalide. Utilise HH:MM (ex: 07:30)")    
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return target