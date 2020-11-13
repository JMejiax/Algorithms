# https://www.hackerrank.com/challenges/queens-attack-2/problem
def queensAttack(n, k, rq, cq, obs):
	dis_up = n-rq
	dis_down = rq-1
	dis_left = cq-1
	dis_right = n-cq
	dis_up_right = n - max(rq, cq)
	dis_down_right = min(n-cq, rq-1)
	dis_up_left = min(n-rq, abs(1-cq))
	dis_down_left = min(rq, cq)-1
	
	for ro, co in obs:
		if (co == cq and ro > rq) and ro-rq < dis_up:
			dis_up = ro-rq-1
		elif (co == cq and ro < rq) and rq-ro < dis_down:
			dis_down = rq-ro-1
		elif (rq == ro and co < cq) and cq-co < dis_left:
			dis_left = cq-co-1
		elif (rq == ro and co > cq) and co-cq < dis_right:
			dis_right = co-cq-1
		elif (ro > rq and co > cq) and (ro-rq == co-cq) and ro-rq < dis_up_right:
			dis_up_right = ro - rq -1;
		elif (ro < rq and co < cq) and (rq-ro == cq-co) and rq-ro < dis_down_left:
			dis_down_left = rq-ro-1
		elif (ro < rq and co > cq) and (rq-ro == co-cq) and rq-ro < dis_down_right:
			dis_down_right = rq-ro-1
		elif (ro > rq and co < cq) and (ro-rq == cq-co) and ro-rq < dis_up_left:
			dis_up_left = ro-rq-1
	
	return dis_up+dis_down+dis_left+dis_right+dis_up_right+dis_down_right+dis_up_left+dis_down_left

n,k = map(int, input().split())
rq, cq = map(int, input().split())
obs = set()
for _ in range(k):
	x,y = map(int, input().split())
	obs.add((x,y))
r = queensAttack(n, k, rq, cq, obs)
print(r)

