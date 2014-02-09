# -*- coding: UTF-8 -*-

import addonHandler
import gui
import wx

addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.manifest['name'] == "NoBeepsSpeechMode":
			if gui.messageBox(
				# Translators: the label of a message box dialog.
				_("You have installed an old and incompatible version of this add-on. Do you want to uninstall the old version?"),
				# Translators: the title of a message box dialog.
				_("Uninstall old add-on"),
				wx.YES|wx.NO|wx.ICON_WARNING) == wx.YES:
					addon.requestRemove()
			break
