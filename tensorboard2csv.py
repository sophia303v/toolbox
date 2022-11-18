# source: https://blog.csdn.net/weixin_40539826/article/details/111083471
# --in_path: input tensorboard event file
# --out_path: output csv file
from tensorboard.backend.event_processing import event_accumulator
import argparse
import pandas as pd
from tqdm import tqdm

def main():
	parser = argparse.ArgumentParser(description='Export tensorboard data')
	parser.add_argument('--in_path',type=str,required=True)
	parser.add_argument('--out_path',type=str,required=True)
	args = parser.parse_args()
	event_data = event_accumulator.EventAccumulator(args.in_path)
	event_data.Reload()

	keys = event_data.scalars.Keys()
	print(keys)
	k = ['step']+keys
	df = pd.DataFrame(columns=keys[1:])
	df_list = []
	for key in tqdm(keys):
		# print(key,event_data.Scalars(key))

		df_list.append(pd.DataFrame(event_data.Scalars(key)))
	df = None
	for idx, df_tmp in enumerate(df_list):
		if idx == 0:
			continue
		if idx == 1:
			df = pd.merge(df_list[0], df_list[1], on='step',how='outer')
		else:
			df = pd.merge(df,df_tmp,on='step',how='outer')
	df.drop(list(df.filter(regex='wall_time')),axis=1).to_csv(args.out_path,index=False,header=k)

	print("SUCCESS!")

if __name__ == '__main__':
	main()
