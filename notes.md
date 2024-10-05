 #   Column                                                          Non-Null Count  Dtype  
---  ------                                                          --------------  -----  
 0   Study ID                                                        247 non-null    object 
 1   Patient ID                                                      247 non-null    object 
 2   Sample ID                                                       247 non-null    object 
 3*   Age                                                             246 non-null    float64
 4   Age at Which Sequencing was Reported (Years)                    247 non-null    object 
 5*   Albumin                                                         246 non-null    float64
 6*   ALK driver                                                      246 non-null    object 
 7   ALK protein change                                              13 non-null     object 
 8   Archer Panel                                                    247 non-null    object 
 9   ARID1A driver                                                   246 non-null    object 
 10  ARID1A protein change                                           21 non-null     object 
 11  BOR                                                             246 non-null    object 
 12  BRAF driver                                                     246 non-null    object 
 13  BRAF protein change                                             14 non-null     object 
 14  Cancer Type                                                     247 non-null    object 
 15  Cancer Type Detailed                                            247 non-null    object 
 16  Clinically reported PD-L1 score                                 246 non-null    float64
 17  CRDB_SURVEY_COMMENTS                                            0 non-null      float64
 18  CT scan type                                                    246 non-null    object 
 19  Impact TMB Percentile (Across All Tumor Types)                  244 non-null    float64
 20  Impact TMB Score                                                244 non-null    float64
 21  Impact TMB Percentile (Within Tumor Type)                       244 non-null    float64
 22  Cytology fixation type                                          30 non-null     object 
 23  Date added to cBioPortal                                        247 non-null    object 
 24  Durable clinical response                                       48 non-null     object 
 25  Date of death                                                   151 non-null    float64
 26  Disease                                                         246 non-null    object 
 27  dNLR                                                            246 non-null    float64
 28  Date of last drug administration                                246 non-null    float64
 29  Drug start date                                                 246 non-null    float64
 30  ECOG                                                            246 non-null    float64
 31  EGFR driver                                                     246 non-null    object 
 32  EGFR protein change                                             28 non-null     object 
 33  ERBB2 driver                                                    246 non-null    object 
 34  ERBB2 protein change                                            22 non-null     object 
 35  Date of Last Contact                                            246 non-null    float64
 36  Fraction Genome Altered                                         247 non-null    float64
 37  Gene Panel                                                      247 non-null    object 
 38  Halo tumor quality score                                        164 non-null    float64
 39  Histology                                                       246 non-null    object 
 40  Was IMPACT done on the same tissue that PD-L1 IHC was done on?  246 non-null    object 
 41  Institute Source                                                247 non-null    object 
 42  IO drug name                                                    246 non-null    object 
 43  Line of therapy                                                 246 non-null    float64
 44  JS PD-L1 score                                                  201 non-null    float64
 45  Manual tumor annotation                                         193 non-null    object 
 46  Metastatic Site                                                 128 non-null    object 
 47  MET driver                                                      246 non-null    object 
 48  MET protein change                                              14 non-null     object 
 49  MGMT Status                                                     0 non-null      float64
 50  Monotherapy vs. Combination                                     246 non-null    object 
 51  Month added to cBioPortal                                       247 non-null    object 
 52  MSI Comment                                                     148 non-null    object 
 53  MSI Score                                                       246 non-null    float64
 54  MSI Type                                                        246 non-null    object 
 55  MSK Slide ID                                                    204 non-null    float64
 56  Mutation Count                                                  242 non-null    float64
 57  Oncotree Code                                                   247 non-null    object 
 58  Overall survival                                                151 non-null    float64
 59  Other Patient ID                                                2 non-null      object 
 60  Pack-year history                                               246 non-null    object 
 61  MSK Pathology Slide Available                                   247 non-null    object 
 62  PD-L1 tissue site                                               246 non-null    object 
 63  PFS date                                                        246 non-null    float64
 64  PFS Months                                                      246 non-null    float64
 65  PFS Status                                                      246 non-null    object 
 66  Primary Tumor Site                                              247 non-null    object 
 67  Clinical trial IRB                                              13 non-null     object 
 68  RET driver                                                      246 non-null    object 
 69  RET protein change                                              12 non-null     object 
 70  ROS1 driver                                                     246 non-null    object 
 71  ROS1 protein change                                             16 non-null     object 
 72  Sample Class                                                    247 non-null    object 
 73  Number of Samples Per Patient                                   247 non-null    int64  
 74  Sample coverage                                                 247 non-null    int64  
 75  Sample Type                                                     247 non-null    object 
 76  Sex                                                             246 non-null    object 
 77  What is the patient's smoking status?                           246 non-null    object 
 78  Somatic Status                                                  247 non-null    object 
 79  SO comments                                                     86 non-null     object 
 80  Status                                                          246 non-null    object 
 81  STK11 driver                                                    246 non-null    object 
 82  STK11 protein change                                            55 non-null     object 
 83  TMB                                                             246 non-null    float64
 84  Tumor Purity                                                    242 non-null    float64
 85  Treatment Setting                                               246 non-null    object 
 86  Is the patient deceased?                                        246 non-null    object 
 87  Week added to cBioPortal                                        247 non-null    object 
 88  WHO Grade                                                       0 non-null      float64

# Parameters
'Age', 'Albumin', 'ALK driver', 'ARID1A driver', 'BRAF driver', 'Cancer Type',
       'Cancer Type Detailed', 'Clinically reported PD-L1 score',
       'CT scan type', 'Impact TMB Percentile (Across All Tumor Types)',
       'Impact TMB Score', 'Impact TMB Percentile (Within Tumor Type)',
       'Date added to cBioPortal', 'Disease', 'dNLR',
       'Date of last drug administration', 'Drug start date', 'ECOG',
       'EGFR driver', 'ERBB2 driver', 'Date of Last Contact',
       'Fraction Genome Altered', 'Gene Panel', 'Histology',
       'Was IMPACT done on the same tissue that PD-L1 IHC was done on?',
       'Institute Source', 'IO drug name', 'Line of therapy', 'MET driver',
       'Monotherapy vs. Combination', 'Month added to cBioPortal', 'MSI Score',
       'MSI Type', 'Mutation Count', 'Oncotree Code', 'Pack-year history',
       'MSK Pathology Slide Available', 'PD-L1 tissue site', 'PFS date',
       'PFS Months', 'PFS Status', 'Primary Tumor Site', 'RET driver',
       'ROS1 driver', 'Sample Class', 'Number of Samples Per Patient',
       'Sample coverage', 'Sample Type', 'Sex',
       'What is the patient's smoking status?', 'Somatic Status', 'Status',
       'STK11 driver', 'TMB', 'Tumor Purity', 'Treatment Setting',
       'Is the patient deceased?', 'Week added to cBioPortal'

 #   Column                                                          Non-Null Count  Dtype  
---  ------                                                          --------------  -----  
 0   Study ID                                                        247 non-null    object 
 1   Patient ID                                                      247 non-null    object 
 2   Sample ID                                                       247 non-null    object 
 3   Age                                                             246 non-null    float64
 4   Age at Which Sequencing was Reported (Years)                    247 non-null    object 
 5   Albumin                                                         246 non-null    float64
 6   ALK driver                                                      246 non-null    object 
 7   Archer Panel                                                    247 non-null    object 
 8   ARID1A driver                                                   246 non-null    object 
 9   BOR                                                             246 non-null    object 
 10  BRAF driver                                                     246 non-null    object 
 11  Cancer Type                                                     247 non-null    object 
 12  Cancer Type Detailed                                            247 non-null    object 
 13  Clinically reported PD-L1 score                                 246 non-null    float64
 14  CT scan type                                                    246 non-null    object 
 15  Impact TMB Percentile (Across All Tumor Types)                  244 non-null    float64
 16  Impact TMB Score                                                244 non-null    float64
 17  Impact TMB Percentile (Within Tumor Type)                       244 non-null    float64
 18  Date added to cBioPortal                                        247 non-null    object 
 19  Disease                                                         246 non-null    object 
 20  dNLR                                                            246 non-null    float64
 21  Date of last drug administration                                246 non-null    float64
 22  Drug start date                                                 246 non-null    float64
 23  ECOG                                                            246 non-null    float64
 24  EGFR driver                                                     246 non-null    object 
 25  ERBB2 driver                                                    246 non-null    object 
 26  Date of Last Contact                                            246 non-null    float64
 27  Fraction Genome Altered                                         247 non-null    float64
 28  Gene Panel                                                      247 non-null    object 
 29  Histology                                                       246 non-null    object 
 30  Was IMPACT done on the same tissue that PD-L1 IHC was done on?  246 non-null    object 
 31  Institute Source                                                247 non-null    object 
 32  IO drug name                                                    246 non-null    object 
 33  Line of therapy                                                 246 non-null    float64
 34  MET driver                                                      246 non-null    object 
 35  Monotherapy vs. Combination                                     246 non-null    object 
 36  Month added to cBioPortal                                       247 non-null    object 
 37  MSI Score                                                       246 non-null    float64
 38  MSI Type                                                        246 non-null    object 
 39  Mutation Count                                                  242 non-null    float64
 40  Oncotree Code                                                   247 non-null    object 
 41  Pack-year history                                               246 non-null    object 
 42  MSK Pathology Slide Available                                   247 non-null    object 
 43  PD-L1 tissue site                                               246 non-null    object 
 44  PFS date                                                        246 non-null    float64
 45  PFS Months                                                      246 non-null    float64
 46  PFS Status                                                      246 non-null    object 
 47  Primary Tumor Site                                              247 non-null    object 
 48  RET driver                                                      246 non-null    object 
 49  ROS1 driver                                                     246 non-null    object 
 50  Sample Class                                                    247 non-null    object 
 51  Number of Samples Per Patient                                   247 non-null    int64  
 52  Sample coverage                                                 247 non-null    int64  
 53  Sample Type                                                     247 non-null    object 
 54  Sex                                                             246 non-null    object 
 55  What is the patient's smoking status?                           246 non-null    object 
 56  Somatic Status                                                  247 non-null    object 
 57  Status                                                          246 non-null    object 
 58  STK11 driver                                                    246 non-null    object 
 59  TMB                                                             246 non-null    float64
 60  Tumor Purity                                                    242 non-null    float64
 61  Treatment Setting                                               246 non-null    object 
 62  Is the patient deceased?                                        246 non-null    object 
 63  Week added to cBioPortal                                        247 non-null    object 

 BOR could be used for competing risks later