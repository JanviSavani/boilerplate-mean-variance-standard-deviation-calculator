import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError('List must contain nine numbers.')
  else:
    m = np.array(list).reshape((3, 3))
    #print(m)
  
    #Mean
    rowmean = m.mean(0)
    colmean = m.mean(1)
    flattenedmean = m.mean()
  
    #Variance
    rowvar = np.var(m, axis=0)
    colvar = np.var(m, axis=1)
    flattenedvar = np.var(m)
  
    #Standard Deviation
    rowstd = np.std(m, axis=0)
    colstd = np.std(m, axis=1)
    flattenedstd = np.std(m)
  
    #Max
    rowmax = m.max(0)
    colmax = m.max(1)
    flattenedmax = m.max()
  
    #Min
    rowmin = m.min(0)
    colmin = m.min(1)
    flattenedmin = m.min()
  
    #Sum
    rowsum = m.sum(0)
    colsum = m.sum(1)
    flattenedsum = m.sum()
  
    calculations = {
      'mean': [rowmean.tolist(), colmean.tolist(), flattenedmean],
      'variance': [rowvar.tolist(), colvar.tolist(), flattenedvar],
      'standard deviation': [rowstd.tolist(), colstd.tolist(), flattenedstd],
      'max': [rowmax.tolist(), colmax.tolist(), flattenedmax],
      'min': [rowmin.tolist(), colmin.tolist(), flattenedmin],
      'sum': [rowsum.tolist(), colsum.tolist(), flattenedsum]
    }
    
    return calculations