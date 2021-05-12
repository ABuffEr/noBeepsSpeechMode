# -*- coding: UTF-8 -*-
#Plugin to switch only between Talk or Off speech modes
#Author: Alberto Buffolino

import addonHandler
import globalPluginHandler
import speech
from . import msg as NVDALocale
addonHandler.initTranslation()

try:
	from globalCommands import SCRCAT_SPEECH
except:
	SCRCAT_SPEECH = None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_SPEECH

	def script_noBeepsSpeechMode(self, gesture):
		curMode = speech.getState().speechMode
		if curMode == speech.SpeechMode.talk:
			NVDALocale.message("Speech mode off")
			speech.setSpeechMode(speech.SpeechMode.off)
		elif curMode == speech.SpeechMode.off:
			speech.setSpeechMode(speech.SpeechMode.talk)
			# Translators: no translation required (see msg.py)
			NVDALocale.message("Speech mode talk")

	# Translators: Message presented in input help mode,
	# this string is partially present in .po localization file of NVDA for the various languages.
	script_noBeepsSpeechMode.__doc__ = _("Toggles between the speech modes of off and talk. When set to off NVDA will not speak anything. If talk then NVDA wil just speak normally.")

	__gestures = {
		"kb:NVDA+s": "noBeepsSpeechMode",
	}