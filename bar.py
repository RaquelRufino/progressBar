from tqdm import tqdm
import time
import requests
from multiprocessing import Pool

chunk_size = 1024

url = "http://sinop.unemat.br/site_antigo/prof/foto_p_downloads/fot_12991calculo_volume_1_james_stewabt_cob_pdf.Calculo_Volume_1_james_stewart_cor.pdf"

r = requests.get(url, stream = True)

total_size = int(r.headers['content-length'])

with Pool(processes=2) as p:
	with open("Calculo1.pdf", "wb") as f:
		for data in tqdm(iterable = r.iter_content(	chunk_size = chunk_size),total = total_size / chunk_size,unit = 'KB'):
			f.write(data)
		
print('Download complete')
