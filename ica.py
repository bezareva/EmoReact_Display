import pyxdf
import mne

from numpy import save


if __name__ == '__main__':
       # for i in range(3):

                #ispitanik = i+1
                ispitanik=1
                #print("[INFO] ICA: ispitanik {}".format(ispitanik))
                file = 'data/vesti_id1.xdf'
                #file = 'data/vesti_id{}.xdf'.format(ispitanik)
                data = pyxdf.load_xdf(file)[0][0]['time_series'] * 40e-9

                chan_ct = len(data.T)
                ch_names = list(["ch{}".format(i) for i in range(chan_ct)])
                info = mne.create_info(ch_names, 250, ch_types=["eeg"] * chan_ct)
                raw = mne.io.RawArray(data.T, info)



                # raw.set_montage("standard_1020")
                raw_tmp = raw.copy()
                raw_tmp.filter(l_freq=1, h_freq=None)
                ica = mne.preprocessing.ICA(method="infomax",
                                           fit_params={"extended": True},
                                           random_state=1)


                ica.fit(raw_tmp, decim=10)


                ica.plot_sources(inst=raw_tmp, show_scrollbars=False)


                ica.exclude = [2]
                raw_corrected = raw.copy()
                ica.apply(raw_corrected)





                raw.plot(n_channels=24, title="Before", duration=12)
                raw_corrected.plot(n_channels=24, title="After", duration=12)


                #file_path = 'data/eeg_ica_id{}.txt'.format(ispitanik)
                #print("[INFO] Saving eeg to {}".format(file_path))
                #data = save(file_path, raw_tmp._data)