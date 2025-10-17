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

try:
    target = parse_time_str(hhmm)
except ValueError as e:
    print("[Erreur]", e)
    raise SystemExit(1)

print("Alarme programmée pour :", target.strftime("%Y-%m-%d %H:%M"))

while True:
    now = datetime.now()
    if now >= target:
        print("\n ALARME !")
        break
    remaining = int((target - now).total_seconds())
    if remaining % 15 ==0:
        m, s = divmod(remaining, 60)
        h, m = divmod(m, 60)
        print(f"Temps restant: {h:02d}:{m:02d}:{s:02d}", end="\r", flush=True)
    time.sleep(0.5)    