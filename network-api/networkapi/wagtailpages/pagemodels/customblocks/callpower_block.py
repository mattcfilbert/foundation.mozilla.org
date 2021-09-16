from wagtail.core import blocks

"""
From https://github.com/OpenSourceActivismTech/call-power/blob/master/INTEGRATION_JS.md#calling-endpoints-directly:

You can trigger a phone call by hitting the /call/create endpoint directly with either a GET or a POST.
URL parameters should include:

    userPhone (required)
    campaignId (required)
    userLocation (optional)
    userCountry (optional)
    ref (optional, limited to 64 characters)

The response will be a JSON object with the following fields:

{
  "call": "queued",
  "campaign": "live", "paused", or "archived",
  "fromNumber": "+18005551212",
  "redirect": null or a URL to redirect to on success,
  "script": "" or an HTML blob to display to the user,
  "targets": {
    "segment": "custom",
    "objects": [
      {
        "name": "",
        "phone": "",
        "title": ""
      },
    ]
    or "display": "Congress" (a string to display for campaigns which do not have pre-set custom targets)
}
"""

class CallpowerBlock(blocks.StructBlock):
    campaignId = blocks.IntegerBlock(
        default=1,
        help_text="The ID number for this campaign. This can be found using the CallPower dashboard.",
    )

    class Meta:
        icon = 'placeholder'
        template = 'wagtailpages/blocks/callpower_block.html'
