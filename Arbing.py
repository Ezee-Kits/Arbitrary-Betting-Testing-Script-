import pandas as pd
import numpy as np
import time


#All Betting Site Gathered Matches  Infomation
betking ={"HomeTeam":["chelsea","manchester city","manchester united","leeds"],

						"AwayTeam":["everton","west ham united","brighton & hove albion","wolverhampton wanderers"],
						"bookmaker":["betking","betking","betking","betking"],
				"h_odd":[2.01,2.2,1.7,1.9],
				"draw":[2.19,2.25,3.25,3.21],
				"a_odd":[3.5,3.31,4.51,5.13]}

bet9ja = {"HomeTeam":["leeds","chelsea","manchester united","manchester city"],
			"AwayTeam":["wolverhampton wanderers","everton","brighton albion","west ham united"],
			"bookmaker":["bet9ja","bet9ja","bet9ja","bet9ja"],
			"h_odd":[2.09,2.21,1.9,2.1],
			"draw":[2.9,2.24,2.00,3.01],
			"a_odd":[5.21,3.4,3.91,3.11]}
			
msport = {"HomeTeam":["chelsea","manchester city","manchester united","leeds"],
				"AwayTeam":["everton","west ham united","brighton & hove albion","wolverhampton wanderers"],
				"bookmaker":["msport","msport","msport","msport"],
				"h_odd":[2.21,2.22,1.71,2.01],
				"draw":[2.13,2.23,3.20,3.3],
				"a_odd":[3.21,3.21,4.3,5.11]}
				
bangbet = {"HomeTeam":["tothenham","manchester city","manchester united","leeds"],
				"AwayTeam":["arsenal","west ham united","brighton & hove albion","wolverhampton wanderers"],
				"bookmaker":["bangbet","bangbet","bangbet","bangbet"],
				"h_odd":[1.91,2.22,1.71,2.01],
				"draw":[3.13,2.21,3.29,3.21],
				"a_odd":[4.12,3.1,4.13,5.11]}
				
				
# All Betting Site Converted To DataFrame Format
				
betking = pd.DataFrame(betking)


bet9ja = pd.DataFrame(bet9ja)

msport = pd.DataFrame(msport)


bangbet = pd.DataFrame(bangbet)



all_data = {"HomeTeam":[],
					"AwayTeam":[],
					"bookmaker":[],
					"h_odd":[],
					"draw":[],
					"a_odd":[]}

#df = pd.DataFrame(all_data)

for k ,clubs in enumerate(betking["HomeTeam"]):
	for i, _1 in enumerate(betking["HomeTeam"]):
		#Bet9ja
		if bet9ja["HomeTeam"][i]==betking["HomeTeam"][k] and bet9ja["AwayTeam"][i]==betking["AwayTeam"][k]:
			all_data["HomeTeam"].append(bet9ja["HomeTeam"][i])
			all_data["AwayTeam"].append(bet9ja["AwayTeam"][i])
			all_data["h_odd"].append(bet9ja["h_odd"][i])
			all_data["draw"].append(bet9ja["draw"][i])
			all_data["a_odd"].append(bet9ja["a_odd"][i])
			all_data["bookmaker"].append(bet9ja["bookmaker"][i])
		else:
			pass
			
			#msport
		if msport["HomeTeam"][i]==betking["HomeTeam"][k] and msport["AwayTeam"][i]==betking["AwayTeam"][k]:
			all_data["HomeTeam"].append(msport["HomeTeam"][i])
			all_data["AwayTeam"].append(msport["AwayTeam"][i])
			all_data["h_odd"].append(msport["h_odd"][i])
			all_data["draw"].append(msport["draw"][i])
			all_data["a_odd"].append(msport["a_odd"][i])
			all_data["bookmaker"].append(msport["bookmaker"][i])
		else:
			pass
			#bangbet
		if bangbet["HomeTeam"][i]==betking["HomeTeam"][k] and bangbet["AwayTeam"][i]==betking["AwayTeam"][k]:
			all_data["HomeTeam"].append(bangbet["HomeTeam"][i])
			all_data["AwayTeam"].append(bangbet["AwayTeam"][i])
			all_data["h_odd"].append(bangbet["h_odd"][i])
			all_data["draw"].append(bangbet["draw"][i])
			all_data["a_odd"].append(bangbet["a_odd"][i])
			all_data["bookmaker"].append(bangbet["bookmaker"][i])
		else:
			pass
			
		#Betking
		if betking["HomeTeam"][i]==betking["HomeTeam"][k] and betking["AwayTeam"][i]==betking["AwayTeam"][k]:
			all_data["HomeTeam"].append(betking["HomeTeam"][i])
			all_data["AwayTeam"].append(betking["AwayTeam"][i])
			all_data["h_odd"].append(betking["h_odd"][i])
			all_data["draw"].append(betking["draw"][i])
			all_data["a_odd"].append(betking["a_odd"][i])
			all_data["bookmaker"].append(betking["bookmaker"][i])
		else:
			pass
	df = pd.DataFrame(all_data)
	for h_i,home in enumerate(df["h_odd"]):
		for d_i,draw in enumerate(df["draw"]):
			for a_i,away in enumerate(df["a_odd"]):
				try:
					print("	")
					print("	**********")
					pr1 = home
					pr2 = draw
					pr3 = away
					
					home_bookmaker= df["bookmaker"][h_i]
					draw_bookmaker = df["bookmaker"][d_i]
					away_bookmaker = df["bookmaker"][a_i]
					
					home_team = df["HomeTeam"][h_i]
					away_team = df["AwayTeam"][a_i]
									
					matcoef = round((1/pr1 + 1/pr2 + 1/pr3)*100)
					if matcoef >= 100:
						print("		")	
						
						print(f"   | {home_bookmaker} (  {home_team }  )  - home odd : {pr1} |  {draw_bookmaker} - draw odd : {pr2} | {away_bookmaker} ( { away_team}  ) - away odd : {pr3} |    {matcoef}% NOT SUITABLE FOR ARBING \n ")
						print(df)
						#time.sleep(5)
					
					if matcoef < 100:
						print("		")
						print(f"    | {home_bookmaker} (  {home_team }  )  - home odd : {pr1} |  {draw_bookmaker} - draw odd : {pr2} | {away_bookmaker} ( { away_team}  ) - away odd : {pr3} |       {matcoef}% ****SUITABLE FOR ARBING,HURRY UP AND BET *****\n")
						print(df)
						time.sleep(2)
						
						amt = float(input("\n	ENTER AMOUNT FOR BETTING:"))
						
						print("		")
						h = round(((amt * 1/pr1)/matcoef)*100)
						print(f"		STAKE : {h} FOR HOME AND WITH MARKET MARGIN OF {round(100-matcoef)}% AND ACTUAL PROFIT TO MAKE OF #{round((h*pr1)-amt)}\n")
						d = round(((amt * 1/pr2)/matcoef)*100)
									
						print(f"		STAKE : {d} FOR DRAW AND WITH MARKET MARGIN OF {round(100-matcoef)}% AND ACTUAL PROFIT TO MAKE OF #{round((d*pr2)-amt)} \n")
						a = round(((amt * 1/pr3)/matcoef)*100)
						print(f"		STAKE : {a} FOR AWAY AND WITH MARKET MARGIN OF #{round(100-matcoef)}% AND ACTUAL PROFIT TO MAKE OF {round((a*pr3)-amt)} \n")
						# IF STATEMENT FOLLOWED BY SELENIUM POSITION
						time.sleep(5)	
				except:
					print("\n	AN ERROR OCCURED DUE TO WRONG KEY PRESS OR WRONG IMFORMATION FORMAT , PLEASE CHECK OUR CREDENTIALS AND TRY AGAIN LATER")
	for info in all_data.values():
		info.clear()	
	
