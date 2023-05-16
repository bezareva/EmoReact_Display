# EmoReact_Display
PyQt5 generated interface for displaying changes in processed
physiological signals (EEG, ECG, GSR). 
<hr>

### Interface:
![display.png](https://raw.githubusercontent.com/bezareva/static/master/EmoReact_Display/display.png)

As can be seen in picture above, app enables user to change:

- Picture of visual stimulus 
- Test subject
- EEG channel
- Frequency band 
After applying changes, user can export data into csv file.

### Signal processing
**EEG signals**

Raw signal

![eeg_before.png](https://raw.githubusercontent.com/bezareva/static/master/EmoReact_Display/eeg_before.png)


Processed signal - Power Sepctral Density
![eeg_PSD.png](https://raw.githubusercontent.com/bezareva/static/master/EmoReact_Display/eeg_PSD.png)


Signal after ICA algorithm - used to clear ocular artifact:
note: channel 19 is ECG signal, all the other are EEG

![EEG_cleared_ICA.png](https://raw.githubusercontent.com/bezareva/static/master/EmoReact_Display/EEG_cleared_ICA.png)



**ECG Signal**

Raw signal:

![ecg_before.png](https://raw.githubusercontent.com/bezareva/static/master/EmoReact_Display/ecg_before.png)



Filtered signal - RR peaks detected:

![ecg_after.png](https://raw.githubusercontent.com/bezareva/static/master/EmoReact_Display/ecg_after.png)

