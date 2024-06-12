def transformada_fourier(sinal):
    fourier = np.fft.fft(sinal)
    return fourier