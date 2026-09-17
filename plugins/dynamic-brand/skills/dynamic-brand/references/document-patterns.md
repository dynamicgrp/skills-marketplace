# Document patterns

Page structures and production notes for Dynamic Group documents. Source: Dynamic Group Brand Guide, September 2026.

## Page types

### Cover

Dark full bleed photography under the scrim so white type reads. Side padding 56px.

Stack, top to bottom: full lockup top left at 30 to 42pt with a drop shadow, cover title at 33.75pt Barlow Semi Condensed ALL CAPS, a short orange rule, then the client name and date in chrome. Nothing else competes.

### Section divider

Same dark photography and scrim treatment as the cover, 56px padding. A two digit section number, the divider title at 40.5pt, and a 5 to 6px orange rule beneath it. One sentence of standfirst is permitted.

### Content page

White paper, 60px side padding. Running header carries the cube and a 2px orange underline. Running footer carries the document name and page number in 8.25pt Barlow chrome. The lockup does not appear on content pages; the cube in the header is the only mark.

Body sets at 11.25pt Source Sans 3. A lead paragraph may open a section at 12.4pt. Section headings are 22.5pt Barlow ALL CAPS, subsections 13.5pt.

### Figure

Rectangular, never rounded beyond the 2px house radius, with the figure shadow. Caption directly beneath in 9.75pt uppercase, client named first, then what is shown.

Example: `CITY OF FORT MYERS. CREW SETTING MODULAR UNITS AT THE PALM AVENUE SITE.`

## Tables

Header band in Dynamic Charcoal with white 9pt Barlow ALL CAPS. Body cells 11.25pt Source Sans 3, or 9.75pt when the table is dense. Interior rules are 1px hairline. The outer border is 1px `#D8D9DB`. Tables and matrices are square, with no corner radius.

Numerals that carry weight, such as unit counts, durations and dollar figures, set in Deep Orange. Let the metric carry the emphasis rather than bolding the sentence around it.

## Rhythm

One marker per page across every list on that page. If a page holds a narrative list and a dense card list, the narrative list takes the diamond and the card list takes the dash, and neither appears twice on the same page in a different form.

One logo per page. One orange device per role. A page with a kicker bar, a section rule, a card top border and a callout left rule at once is over specified. Pick the devices the content needs.

## PDF production

The established Dynamic workflow generates with ReportLab and manipulates with pymupdf and fonttools.

Font files come from the Google Fonts GitHub repository, which carries the full weight range rather than the subset a web request returns. Both families are there: `barlowsemicondensed` and `sourcesans3`. Embed full font files rather than relying on a system install.

Embed text into the page content stream rather than as annotations. Annotation based text does not survive Adobe reliably.

When generating from HTML, load `tokens.css` and render at 816 by 1056px so the px geometry maps one to one onto US Letter at 96dpi. No scaling step is needed.

## Reviewing existing material

Check in this order, because the early failures are the ones that read as unprofessional fastest:

1. Em dashes, emoji, exclamation points. These are banned outright.
2. Third person self reference. Any instance of the firm, its, or itself describing Dynamic.
3. Addressing the client as you rather than by title.
4. Phone number format. It is `(###) ###-####` with a space after the area code.
5. Color. Any blue, purple, gradient other than the cover scrim, or the superseded `#F58132` orange.
6. Type. All caps runs inside paragraphs, body copy off 11.25pt, or Barlow set in sentence case.
7. Logo. Recolored, stretched, duplicated on one page, or under 21pt without falling back to the cube.
8. Lists. More than one marker on a page, or icons on every list.

Report the specific failure and the correction. A general impression is not useful to someone trying to ship a document.
