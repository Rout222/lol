import MySQLdb
import click

champs = {
	62: [62, 'MonkeyKing', 'MonkeyKing_vxuea2'],
	24: [24, 'Jax', 'Jax_uvpgkq'],
	9: [9, 'Fiddlesticks', 'Fiddlesticks_jb8isc'],
	35: [35, 'Shaco', 'Shaco_cmw8bi'],
	19: [19, 'Warwick', 'Warwick_pmrx0x'],
	498: [498, 'Xayah', 'Xayah_wjn3ve'],
	76: [76, 'Nidalee', 'Nidalee_onjloi'],
	143: [143, 'Zyra', 'Zyra_rhatdv'],
	240: [240, 'Kled', 'Kled_iwalhi'],
	63: [63, 'Brand', 'Brand_ladogh'],
	33: [33, 'Rammus', 'Rammus_iahegv'],
	420: [420, 'Illaoi', 'Illaoi_bhvo0a'],
	42: [42, 'Corki', 'Corki_a8gjdm'],
	201: [201, 'Braum', 'Braum_fn5u2s'],
	122: [122, 'Darius', 'Darius_sgadhh'],
	23: [23, 'Tryndamere', 'Tryndamere_f163dt'],
	21: [21, 'MissFortune', 'MissFortune_o7n6az'],
	83: [83, 'Yorick', 'Yorick_cyfuan'],
	101: [101, 'Xerath', 'Xerath_iky0dg'],
	15: [15, 'Sivir', 'Sivir_fib6pk'],
	92: [92, 'Riven', 'Riven_k5uhr6'],
	61: [61, 'Orianna', 'Orianna_wb9fr0'],
	41: [41, 'Gangplank', 'Gangplank_mu92at'],
	54: [54, 'Malphite', 'Malphite_opbb29'],
	78: [78, 'Poppy', 'Poppy_apyzn3'],
	30: [30, 'Karthus', 'Karthus_ti1grw'],
	126: [126, 'Jayce', 'Jayce_efliq5'],
	20: [20, 'Nunu', 'Nunu_iyzaqy'],
	48: [48, 'Trundle', 'Trundle_unlfru'],
	104: [104, 'Graves', 'Graves_y3nbr6'],
	142: [142, 'Zoe', 'Zoe_ebcvnx'],
	150: [150, 'Gnar', 'Gnar_x4pchb'],
	99: [99, 'Lux', 'Lux_pgtgbi'],
	102: [102, 'Shyvana', 'Shyvana_ae38l6'],
	58: [58, 'Renekton', 'Renekton_ct3fdv'],
	114: [114, 'Fiora', 'Fiora_mm5wzj'],
	222: [222, 'Jinx', 'Jinx_gfpoju'],
	429: [429, 'Kalista', 'Kalista_vsvon0'],
	105: [105, 'Fizz', 'Fizz_y6w3ly'],
	38: [38, 'Kassadin', 'Kassadin_z31nwe'],
	37: [37, 'Sona', 'Sona_wscawa'],
	39: [39, 'Irelia', 'Irelia_g95etq'],
	112: [112, 'Viktor', 'Viktor_zcmlct'],
	497: [497, 'Rakan', 'Rakan_yggftl'],
	203: [203, 'Kindred', 'Kindred_iwfh9p'],
	69: [69, 'Cassiopeia', 'Cassiopeia_m03xgf'],
	57: [57, 'Maokai', 'Maokai_fgqz2s'],
	516: [516, 'Ornn', 'Ornn_jfxv6t'],
	412: [412, 'Thresh', 'Thresh_eowzxf'],
	10: [10, 'Kayle', 'Kayle_ite8x6'],
	120: [120, 'Hecarim', 'Hecarim_nxa7k6'],
	121: [121, 'Khazix', 'Khazix_ornb6c'],
	2: [2, 'Olaf', 'Olaf_gb1q6m'],
	115: [115, 'Ziggs', 'Ziggs_hs36zc'],
	134: [134, 'Syndra', 'Syndra_e5x0dw'],
	36: [36, 'DrMundo', 'DrMundo_f2i6ws'],
	43: [43, 'Karma', 'Karma_vabogg'],
	1: [1, 'Annie', 'Annie_vxmi7u'],
	84: [84, 'Akali', 'Akali_ctsv58'],
	106: [106, 'Volibear', 'Volibear_zrzz2t'],
	157: [157, 'Yasuo', 'Yasuo_fwddlb'],
	85: [85, 'Kennen', 'Kennen_tjo71v'],
	107: [107, 'Rengar', 'Rengar_pvtzrd'],
	13: [13, 'Ryze', 'Ryze_u8qvmi'],
	98: [98, 'Shen', 'Shen_oz3nur'],
	154: [154, 'Zac', 'Zac_sktndb'],
	91: [91, 'Talon', 'Talon_jhv1ip'],
	50: [50, 'Swain', 'Swain_gsgrf8'],
	432: [432, 'Bard', 'Bard_dvkodr'],
	14: [14, 'Sion', 'Sion_euybyi'],
	67: [67, 'Vayne', 'Vayne_citiq9'],
	75: [75, 'Nasus', 'Nasus_d8lu6z'],
	141: [141, 'Kayn', 'Kayn_yvi1ng'],
	4: [4, 'TwistedFate', 'TwistedFate_cebtep'],
	31: [31, 'Chogath', 'Chogath_fpaid6'],
	77: [77, 'Udyr', 'Udyr_zvln3g'],
	236: [236, 'Lucian', 'Lucian_o8ymah'],
	427: [427, 'Ivern', 'Ivern_rmgp3v'],
	89: [89, 'Leona', 'Leona_vtnfcf'],
	51: [51, 'Caitlyn', 'Caitlyn_enbgus'],
	113: [113, 'Sejuani', 'Sejuani_wgkwz4'],
	56: [56, 'Nocturne', 'Nocturne_pmvgif'],
	26: [26, 'Zilean', 'Zilean_xrvrzh'],
	268: [268, 'Azir', 'Azir_irtk6u'],
	68: [68, 'Rumble', 'Rumble_qz65ab'],
	25: [25, 'Morgana', 'Morgana_i3dlxw'],
	163: [163, 'Taliyah', 'Taliyah_tmbggc'],
	17: [17, 'Teemo', 'Teemo_r6iodt'],
	6: [6, 'Urgot', 'Urgot_bilkav'],
	32: [32, 'Amumu', 'Amumu_euqkbi'],
	3: [3, 'Galio', 'Galio_zssmmw'],
	74: [74, 'Heimerdinger', 'Heimerdinger_pctrrj'],
	34: [34, 'Anivia', 'Anivia_zcbjor'],
	22: [22, 'Ashe', 'Ashe_ca5ls0'],
	161: [161, 'Velkoz', 'Velkoz_cqmp2m'],
	27: [27, 'Singed', 'Singed_qmbcjf'],
	72: [72, 'Skarner', 'Skarner_x8alx1'],
	110: [110, 'Varus', 'Varus_ixtiwy'],
	29: [29, 'Twitch', 'Twitch_do2vya'],
	86: [86, 'Garen', 'Garen_kgejh8'],
	53: [53, 'Blitzcrank', 'Blitzcrank_wtp21f'],
	11: [11, 'MasterYi', 'MasterYi_xbwndn'],
	60: [60, 'Elise', 'Elise_fwfnw3'],
	12: [12, 'Alistar', 'Alistar_ndw3sn'],
	55: [55, 'Katarina', 'Katarina_u0kdky'],
	245: [245, 'Ekko', 'Ekko_aefzsk'],
	82: [82, 'Mordekaiser', 'Mordekaiser_nv0kci'],
	117: [117, 'Lulu', 'Lulu_hdqisp'],
	164: [164, 'Camille', 'Camille_zeu1xi'],
	266: [266, 'Aatrox', 'Aatrox_sjjmj0'],
	119: [119, 'Draven', 'Draven_fpcqq3'],
	223: [223, 'TahmKench', 'TahmKench_tfuuoe'],
	80: [80, 'Pantheon', 'Pantheon_y9ccpv'],
	5: [5, 'XinZhao', 'XinZhao_fon5la'],
	136: [136, 'AurelionSol', 'AurelionSol_wqi3wt'],
	64: [64, 'LeeSin', 'LeeSin_knukr5'],
	44: [44, 'Taric', 'Taric_lh7crm'],
	90: [90, 'Malzahar', 'Malzahar_baspfj'],
	127: [127, 'Lissandra', 'Lissandra_gaeehw'],
	131: [131, 'Diana', 'Diana_jhvafx'],
	18: [18, 'Tristana', 'Tristana_q3a4p1'],
	421: [421, 'RekSai', 'RekSai_fe1wdo'],
	8: [8, 'Vladimir', 'Vladimir_jc1kpf'],
	59: [59, 'JarvanIV', 'JarvanIV_zt9yjw'],
	267: [267, 'Nami', 'Nami_jz2e7c'],
	202: [202, 'Jhin', 'Jhin_z7voxd'],
	16: [16, 'Soraka', 'Soraka_fofe4o'],
	45: [45, 'Veigar', 'Veigar_ttbsrx'],
	40: [40, 'Janna', 'Janna_e9qtxt'],
	111: [111, 'Nautilus', 'Nautilus_huhugq'],
	28: [28, 'Evelynn', 'Evelynn_noivi3'],
	79: [79, 'Gragas', 'Gragas_ciptaz'],
	238: [238, 'Zed', 'Zed_r2zriz'],
	254: [254, 'Vi', 'Vi_km3pjd'],
	96: [96, 'KogMaw', 'KogMaw_eayglp'],
	103: [103, 'Ahri', 'Ahri_j3avlb'],
	133: [133, 'Quinn', 'Quinn_pf6oa5'],
	7: [7, 'Leblanc', 'Leblanc_h0ysgr'],
	81: [81, 'Ezreal', 'Ezreal_ejzzsi']}

def execute_query(string):
	db=MySQLdb.connect(passwd="",db="leagueoflegends", user="root")
	c=db.cursor()
	c.execute(string)
	db.commit()
	db.close()

def clear_champions():
	execute_query("TRUNCATE champs")

def insert_all_champions():
	with click.progressbar(champs.items(), label='Inserindo Novos Dados na tabela') as bar:
		for uid,x in bar:
			execute_query("INSERT INTO `champs`(`name`, `url`, `uid`) VALUES (\"{}\",\"{}\",\"{}\")".format(str(x[1]),str(x[2]),str(x[0])))

def reset_champions():
	clear_champions()
	insert_all_champions();
