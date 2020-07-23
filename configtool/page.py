from __future__ import print_function

import wx

from configtool.decoration import Decoration
from configtool.data import reInteger, reFloat, offsetChLabel, offsetTcLabel, pinNames


class Page:
    def __init__(self, font):
        self.modified = False
        self.valid = True
        self.fieldValid = {}
        self.textControls = {}
        self.textControlsOriginal = {}
        self.checkBoxes = {}
        self.radioButtons = {}
        self.radioButtonBoxes = {}
        self.choices = {}
        self.choicesOriginal = {}
        self.boolChoices = {}
        self.deco = Decoration()
        self.font = font

        self.SetBackgroundColour(self.deco.getBackgroundColour())
        self.Bind(wx.EVT_PAINT, self.deco.onPaintBackground)

    def enableAll(self, flag=True):
        for c in self.textControls.keys():
            self.textControls[c].Enable(flag)
        for c in self.checkBoxes.keys():
            self.checkBoxes[c].Enable(flag)
        for c in self.radioButtons.keys():
            self.radioButtons[c].Enable(flag)
        for c in self.choices.keys():
            self.choices[c].Enable(flag)

    def addTextCtrl(self, name, labelWidth, validator):
        lsz = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(
            self,
            wx.ID_ANY,
            self.labels[name] + " ",
            size=(labelWidth, -1),
            style=wx.ALIGN_RIGHT,
        )
        st.SetFont(self.font)
        lsz.Add(st, 1, wx.TOP, offsetTcLabel)

        tc = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_RIGHT, name=name)
        tc.SetFont(self.font)
        self.fieldValid[name] = True
        tc.Bind(wx.EVT_TEXT, validator)
        self.textControls[name] = tc
        lsz.Add(tc)

        return lsz

    def addCheckBox(self, name, validator):
        if name in self.labels.keys():
            lbl = self.labels[name]
        else:
            lbl = name
        cb = wx.CheckBox(self, wx.ID_ANY, lbl)
        cb.SetFont(self.font)
        cb.Bind(wx.EVT_CHECKBOX, validator)
        self.checkBoxes[name] = cb

        return cb

    def addRadioButton(self, name, style, validator, sbox=None):
        rb = wx.RadioButton(self, wx.ID_ANY, self.labels[name], style=style)
        rb.SetFont(self.font)
        self.Bind(wx.EVT_RADIOBUTTON, validator, rb)
        self.radioButtons[name] = rb
        if sbox is not None:
            self.radioButtonBoxes[name] = sbox

        return rb

    def addChoice(self, name, choices, selection, labelWidth, validator, size=(-1, -1)):
        lsz = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(
            self,
            wx.ID_ANY,
            self.labels[name],
            size=(labelWidth, -1),
            style=wx.ALIGN_RIGHT,
        )
        st.SetFont(self.font)
        lsz.Add(st, 1, wx.TOP, offsetChLabel)

        ch = wx.Choice(self, wx.ID_ANY, choices=choices, size=size, name=name)
        ch.SetBackgroundColour(self.deco.getBackgroundColour())
        ch.SetFont(self.font)
        ch.Bind(wx.EVT_CHOICE, validator)
        ch.SetSelection(selection)
        lsz.Add(ch)
        self.choices[name] = ch

        return lsz

    def addPinChoice(self, name, labelWidth):
        lsz = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(
            self,
            wx.ID_ANY,
            self.labels[name],
            size=(labelWidth, -1),
            style=wx.ALIGN_RIGHT,
        )
        st.SetFont(self.font)
        lsz.Add(st, 1, wx.TOP, offsetChLabel)

        ch = wx.Choice(self, wx.ID_ANY, name=name, style=wx.CB_SORT)
        ch.SetBackgroundColour(self.deco.getBackgroundColour())
        ch.SetFont(self.font)
        ch.AppendItems(["-"] + pinNames)
        ch.Bind(wx.EVT_CHOICE, self.onChoice)
        self.choices[name] = ch
        lsz.Add(ch)

        return lsz

    # addChoice handles #defines with value, this handles choices for
    # sets of boolean #defines.
    def addBoolChoice(self, name, allowBlank, labelWidth, validator, size=(-1, -1)):
        lsz = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(
            self,
            wx.ID_ANY,
            self.labels[name],
            size=(labelWidth, -1),
            style=wx.ALIGN_RIGHT,
        )
        st.SetFont(self.font)
        lsz.Add(st, 1, wx.TOP, offsetChLabel)

        ch = wx.Choice(self, wx.ID_ANY, size=size, name=name)
        ch.SetBackgroundColour(self.deco.getBackgroundColour())
        ch.SetFont(self.font)
        ch.Bind(wx.EVT_CHOICE, validator)

        if allowBlank:
            ch.Append("(none)")
            ch.SetSelection(0)

        lsz.Add(ch)
        self.boolChoices[name] = ch

        return lsz

    def setChoice(self, name, cfgValues, default):
        if name in cfgValues.keys() and cfgValues[name][1] == True:
            bv = cfgValues[name][0]
        else:
            bv = default

        s = self.choices[name].FindString(bv)
        if s < 0:
            s = self.choices[name].FindString(default)
            if s < 0:
                s = 0

        self.choices[name].SetSelection(s)

    def onTextCtrlInteger(self, evt):
        self.assertModified(True)
        tc = evt.GetEventObject()
        name = tc.GetName()
        w = tc.GetValue().strip()
        if w == "":
            valid = True
        else:
            m = reInteger.match(w)
            if m:
                valid = True
            else:
                valid = False

        self.setFieldValidity(name, valid)

        if valid:
            tc.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        else:
            tc.SetBackgroundColour("pink")
        tc.Refresh()
        evt.Skip()

    def onTextCtrlFloat(self, evt):
        self.assertModified(True)
        tc = evt.GetEventObject()
        name = tc.GetName()
        w = tc.GetValue().strip()
        if w == "":
            valid = True
        else:
            m = reFloat.match(w)
            if m:
                valid = True
            else:
                valid = False

        self.setFieldValidity(name, valid)

        if valid:
            tc.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        else:
            tc.SetBackgroundColour("pink")
        tc.Refresh()
        evt.Skip()

    def onTextCtrlPin(self, evt):
        self.assertModified(True)
        tc = evt.GetEventObject()
        self.validatePin(tc)
        evt.Skip()

    def onTextCtrl(self, evt):
        self.assertModified(True)
        evt.Skip()

    def onChoice(self, evt):
        self.assertModified(True)
        evt.Skip()

    def onCheckBox(self, evt):
        self.assertModified(True)
        evt.Skip()

    def setHelpText(self, ht):
        for k in self.textControls.keys():
            if k in ht.keys():
                self.textControls[k].SetToolTip(ht[k])

        for k in self.checkBoxes.keys():
            if k in ht.keys():
                self.checkBoxes[k].SetToolTip(ht[k])

        for k in self.radioButtons.keys():
            if k in ht.keys():
                self.radioButtons[k].SetToolTip(ht[k])
                if k in self.radioButtonBoxes.keys():
                    self.radioButtonBoxes[k].SetToolTip(ht[k])

        for k in self.choices.keys():
            if k in ht.keys():
                self.choices[k].SetToolTip(ht[k])

        for k in self.boolChoices.keys():
            for candidate in ht.keys():
                if candidate.startswith(k):
                    self.boolChoices[k].SetToolTip(ht[candidate])
                    break

    def insertValues(self, cfgValues):
        self.assertValid(True)
        self.enableAll(True)
        for k in self.fieldValid.keys():
            self.fieldValid[k] = True

        for k in self.checkBoxes.keys():
            if k in cfgValues.keys() and cfgValues[k]:
                self.checkBoxes[k].SetValue(True)
            else:
                self.checkBoxes[k].SetValue(False)

        for k in self.textControls.keys():
            if k in cfgValues.keys():
                self.textControlsOriginal[k] = cfgValues[k]
                if cfgValues[k][1] == True:
                    self.textControls[k].SetValue(str(cfgValues[k][0]))
                else:
                    self.textControls[k].SetValue("")
            else:
                print("Key " + k + " not found in config data.")

        for k in self.choices.keys():
            if k in cfgValues.keys():
                self.choicesOriginal[k] = cfgValues[k]
                self.setChoice(k, cfgValues, "-")
            else:
                print("Key " + k + " not found in config data.")

        for k in self.boolChoices.keys():
            choice = self.boolChoices[k]

            # Remove items left behind from the previous configuration.
            while choice.GetCount() and not choice.GetString(
                choice.GetCount() - 1
            ).startswith("("):
                choice.Delete(choice.GetCount() - 1)

            # Add items found in this configuration.
            for cfg in cfgValues.keys():
                if cfg.startswith(k):
                    if cfg in self.labels.keys():
                        choice.Append(self.labels[cfg])
                    else:
                        choice.Append(cfg)

                    # As we want to write the configuration name later, not the user
                    # friendly string, we store the configuration name as client data.
                    n = choice.GetCount() - 1
                    choice.SetClientData(n, cfg)

                    if cfgValues[cfg]:
                        choice.SetSelection(n)

        self.assertModified(False)

    def getValues(self):
        self.assertModified(False)
        result = {}

        for k in self.checkBoxes.keys():
            cb = self.checkBoxes[k]
            result[k] = cb.IsChecked()

        for k in self.textControls.keys():
            v = self.textControls[k].GetValue()
            if v == "":
                if k in self.textControlsOriginal.keys():
                    result[k] = self.textControlsOriginal[k][0], False
                else:
                    result[k] = "", False
            else:
                result[k] = v, True

        for k in self.radioButtons.keys():
            result[k] = self.radioButtons[k].GetValue(), True

        for k in self.choices.keys():
            v = self.choices[k].GetSelection()
            s = self.choices[k].GetString(v)
            if s == "-":
                if k in self.choicesOriginal.keys():
                    result[k] = self.choicesOriginal[k][0], False
                else:
                    result[k] = "", False
            else:
                result[k] = s, True

        for k in self.boolChoices.keys():
            choice = self.boolChoices[k]
            for i in range(choice.GetCount()):
                s = choice.GetClientData(i)
                if s:
                    result[s] = i == choice.GetSelection()

        return result

    def assertModified(self, flag):
        if flag != self.modified:
            self.parent.assertModified(self.id, flag)
            self.modified = flag

    def setFieldValidity(self, name, flag):
        self.fieldValid[name] = flag

        pgValid = True
        for k in self.fieldValid.keys():
            if not self.fieldValid[k]:
                pgValid = False
                break

        self.assertValid(pgValid)

    def assertValid(self, flag):
        if flag != self.valid:
            self.parent.assertValid(self.id, flag)
            self.valid = flag
