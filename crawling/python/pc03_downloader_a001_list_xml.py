exec(open("C:/Users/Encaion/Documents/41_outsource/crawling_DART_package/crawling/python/pc01_environment.py").read())

# set working directory
os.chdir(mainDir + corps_code_parsed_csv_Dir)

# loading required libraries
import pandas as pd

corps_code_a001 = pd.read_csv("corps_code_parsed_" + base_date + ".csv")

date_begin_a001 = "19800101"
date_end_a001 = base_date
last_reprt_at_a001 = "Y"
pblntf_ty_a001 = "A"
pblntf_detail_ty_a001 = "A001"
page_count_a001 = 100

start_a001 = 1
end_a001 = nrow(corps_code_a001)
time_delay_a001 = 5

for(i in start_a001:end_a001){
  print(i)
  corp_code_a001 = sprintf(fmt = "%08d", corps_code_a001[i, "corp_code"])
  corp_name_a001 = corps_code_a001[i, "corp_name"]
  
  request_url_a001 = paste0("https://opendart.fss.or.kr/api/list.xml?",
                             "&crtfc_key=", key_dart,
                             "&corp_code=", corp_code_a001,
                             "&bgn_de=", date_begin_a001,
                             "&end_de=", date_end_a001,
                             "&last_reprt_at", last_reprt_at_a001,
                             "&pblntf_ty=", pblntf_ty_a001,
                             "&pblntf_detail_ty=", pblntf_detail_ty_a001,
                             "&page_count=", page_count_a001)
  
  report_a001 = read_html(request_url_a001, encoding = "UTF-8")
  write_xml(report_a001, 
            paste0(mainDir, biz_report_list_xml_Dir, "a001_", corp_code_a001, ".xml"), 
            encoding = "UTF-8")
  
  Sys.sleep(time_delay_a001 + runif(1) * 2)
}