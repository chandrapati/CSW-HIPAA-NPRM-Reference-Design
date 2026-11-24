"""Framing text for HIPAA 2025 NPRM. Everything else is read from the design."""

DESIGN = 'CSW-HIPAA-NPRM-Reference-Design.md'

TREE = None

WORKFLOW = {'caution': 'Physical access, HR/training records, encryption key management, signed '
            'BAAs/vendor contracts, formal pen tests, and assessor attestation still require '
            'separate programmes.',
 'caution_label': 'Boundary &rsaquo;',
 'kicker': 'HIPAA 2025 NPRM',
 'rail': ['Machine-generated flow evidence, not hand-drawn diagrams',
          'Simulation proves the policy before anything is enforced',
          'Quarterly packs carry the evidence between assessments'],
 'sub': 'From agent coverage to continuous proof between assessments &mdash; exports map to '
        'control IDs in the Reporting & Evidence section.',
 'takeaway': 'CSW turns observed traffic into designed isolation and keeps producing evidence '
             'after the project ends. <b>The quarterly pack is the deliverable</b> &mdash; it '
             'is what an assessor consumes without a live walkthrough.',
 'title_tail': '&mdash; HIPAA 2025 NPRM'}

PHASES = None
