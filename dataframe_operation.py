# change the image paths of dataframe

dataset_dir = 'somepath'

df = pd.read_csv('{dataset_dir}/thecsv.csv')
df['image_path'] = df.image_path.apply(lambda x: x.replace('the original path', dataset_dir))
