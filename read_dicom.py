import pydicom

def dicom_to_dict(file_path, rles_df, encoded_pixels=True):
    '''
    Get the information of dicom and encoded_pixles
    '''
    
    data = {}
    
    # Parse fields with the meaningful information
    pydicom.dcmread(file_path)
    data['patient_name'] = dicom_data.PatientName
    data['patient_id'] = dicom_data.PatientID
    data['patient_age'] = int(dicom_data.PatientAge)
    data['patient_sex'] = dicom_data.PatientSex
    data['Rows'] = dicom_data.Rows
    data['Columns'] = dicom_data.Columns
    data['pixel_spacing'] = dicom_data.PixelSpacing
    data['file_path'] = file_path
    data['id'] = dicom_data.SOPInstanceUID
    
    # look for annotation if enabled (train set)
    if encoded_pixels:
        encoded_pixels_list = rles_df[rles_df['ImageId'] == dicom_data.SOPInstanceUID]['EncodedPixels'].values
        
        pneu = False
        for encoded_pixels in encoded_pixels_list:
            if encoded_pixels != ' -1':
                penu = True
        
        data['encoded_pixels_list'] = encoded_pixels_list
        data['has_pneumothorax'] = pneu
        data['encoded_pixels_count'] = len(encoded_pixels_list)
        
    return data
