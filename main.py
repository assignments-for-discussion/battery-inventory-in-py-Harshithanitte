
def calculate_soh(present_capacity, rated_capacity=120):
    soh = (present_capacity / rated_capacity) * 100
    return soh


def count_batteries_by_health(present_capacities):
 
    healthy = 0
    exchange = 0
    failed = 0

    for capacity in present_capacities:
        soh = calculate_soh(capacity)
        print(f"present capacity: {capacity},SoH:{soh}")

        if soh > 80 and soh<100:
            healthy += 1
        elif 62 <= soh <= 80:
            exchange += 1
        elif soh < 62.8:
            failed += 1
    print(healthy,exchange,failed)
    
    return {
    "healthy": healthy,
    "exchange": exchange,
    "failed": failed
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  print(counts)
  assert counts["healthy"] == 2
  assert counts["exchange"] == 3
  assert counts["failed"] == 1
  print("Done counting :)")
  
if __name__ == '__main__':
  test_bucketing_by_health()
