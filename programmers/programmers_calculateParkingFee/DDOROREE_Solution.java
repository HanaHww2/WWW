import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class CumulativeCharge {
	private String inTime;
	private int cumulativeTime;
	private int charge;

	public int getCharge() {
		return charge;
	}

	public void setCharge(int charge) {
		this.charge = charge;
	}

	public String getInTime() {
		return inTime;
	}

	public int getCumulativeTime() {
		return cumulativeTime;
	}

	public void setInTime(String inTime) {
		this.inTime = inTime;
	}

	public void setCumulativeTime(int cumulativeTime) {
		this.cumulativeTime = cumulativeTime;
	}

	public CumulativeCharge(String inTime, int cumulativeTime) {
		super();
		this.inTime = inTime;
		this.cumulativeTime = cumulativeTime;
	}
}

class Solution {
	public List<Integer> solution(int[] fees, String[] records) {
		Map<String, CumulativeCharge> recordSet = new HashMap<String, CumulativeCharge>();
		List<Integer> charges = new ArrayList<Integer>();

		/* 차번호 별 누적시간 계산 */
		for (int i = 0; i < records.length; i++) {
			String[] rawRecord = records[i].split(" ");
			CumulativeCharge record = new CumulativeCharge(rawRecord[0], 0);

			// 이미 키가 있는 경우는 in으로 들어왔었다는 것
			if (recordSet.containsKey(rawRecord[1])) {
				record = recordSet.get(rawRecord[1]);
				if (recordSet.get(rawRecord[1]).getInTime() != null) { // 1번 이상 들어온 차들은 누적값을 위해 in 시간만 갱신
					// 기존 누적 시간 + 새로운 주차 시간
					record.setCumulativeTime(
						record.getCumulativeTime()
							+ calculationCumulativeTime(rawRecord[0], record.getInTime())
					);
					record.setInTime(null);
				} else {
					record.setInTime(rawRecord[0]);
				}
				continue;
			}

			recordSet.put(rawRecord[1], record);
		}

		/*
		  	누적 주차시간	<= 기본시간      : 기본요금
			            	>                : 기본요금+[누적시간-기본시간/단위시간]*단위요금
		*/
		for (String key : recordSet.keySet()) {
			int fee = fees[1];
			CumulativeCharge charge = recordSet.get(key);

			// null이 아니란 소리는 out이 안나왔기 때문에 null 처리 작업을 안거쳤단 소리. 그거는 다 2359으로 처리
			if (charge.getInTime() != null) {
				charge.setCumulativeTime( charge.getCumulativeTime()+calculationCumulativeTime("23:59",charge.getInTime()) );
			}

			// 기준요금 여부 판단
			if (charge.getCumulativeTime() > fees[0]) {
				int subtraction = charge.getCumulativeTime() - fees[0];
				int quotient = subtraction / fees[2];
				if (subtraction % fees[2] != 0) {
					quotient = (int)Math.ceil((double)(subtraction) / fees[2]);
				}
				fee += quotient * fees[3];
			}

			charge.setCharge(fee);
		}

		/* 차번호가 작은 순서대로 key 정렬 */
		Object[] mapKey = recordSet.keySet().toArray();
		Arrays.sort(mapKey);

		/* 정렬한 키 기준으로 결과 리스트의 데이터 추출 */
		for (int i = 0; i < mapKey.length; i++) {
			charges.add(recordSet.get(mapKey[i]).getCharge());
		}

		return charges;
	}

	/* 시 -> 분 후, 주차시간 계산 */
	public static int calculationCumulativeTime(String rawOutTime, String rawInTime) {
		String[] outTimes = rawOutTime.split(":");
		String[] inTimes = rawInTime.split(":");
		int outTime = Integer.parseInt(outTimes[0]) * 60 + Integer.parseInt(outTimes[1]);
		int inTime = Integer.parseInt(inTimes[0]) * 60 + Integer.parseInt(inTimes[1]);
		return outTime - inTime;
	}
}