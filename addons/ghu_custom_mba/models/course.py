from odoo import models, fields


class GhuCourse(models.Model):
    _name = 'ghu_custom_mba.course'
    _rec_name = 'name'
    _description = "Course"
    
    name = fields.Char('Name', size=128, required=True)
    long_name = fields.Char('Long Name', size=256, required=True)
    description = fields.Html(
        string=u'Description',
    )

    aims = fields.Html(
        string=u'Aims',
    )

    # Learning Outcomes
    knowledge = fields.Html(
        string=u'Knowledge',
    )

    
    skills = fields.Html(
        string=u'Skills',
    )
    
    
    syllabus = fields.Html(
        string=u'Syllabus',
    )

    
    strategies = fields.Html(
        string=u'Learning, Teaching and Assessment Strategies',
    )
    
    assessment_ids = fields.One2many(
        string=u'Assessments',
        comodel_name='ghu_custom_mba.assessment',
        inverse_name='course_id',
    )
    
    shortcode = fields.Char('Short Code', size=256, required=False)

    language = fields.Many2one(
        string=u'Language',
        comodel_name='ghu.lang',
        required=True,
    )

    program_id = fields.Many2one(
        string=u'Program',
        comodel_name='ghu.program',
    )
    
    script_file = fields.Binary('Script', required=False)
    script_file_filename = fields.Char(
        string=u'Script Filename',
    )

    author_id = fields.Many2one(
        string=u'Author',
        comodel_name='ghu.advisor',
        domain=[('is_cafeteria', '=', 'True')],
    )

    panopto_id = fields.Char('Panopto ID', size=256, required=False)

    creditpoints = fields.Char('Creditpoints Description', size=256, required=False)

    

    # Workflow specifics
    formal_check_done = fields.Boolean(
        string=u'Formal check done?',
    )
    formal_check = fields.Boolean(
        string=u'Formal check result',
    )
    formal_reason = fields.Text(
        string=u'Formal check reason',
    )
    content_check_done = fields.Boolean(
        string=u'Content check done?',
    )
    content_check = fields.Boolean(
        string=u'Content check',
    )
    content_reason = fields.Text(
        string=u'Content check reason',
    )
    
    states = [
        ('draft', 'Draft'), # Created by Lecturer but not finished configuration
        ('new', 'New'), # Submitted by Lecturer but not finished formal and content check
        ('approved', 'Approved'), # Module is checked for content and formal, published
        ('declined', 'Declined'), # Module is checked but didn't met requirements
        ('outdated', 'Outdated'), # Module has to be revised
    ]


class GhuAssessment(models.Model):
    _name = 'ghu_custom_mba.assessment'
    _rec_name = 'name'
    _description = "Assessment"

    
    course_id = fields.Many2one(
        string=u'Course',
        comodel_name='ghu_custom_mba.course',
        ondelete='cascade',
    )
    

    name = fields.Char('Name', size=128, required=True)

    type = fields.Selection(
        string=u'Assessment Type',
        selection=[
            ('essay', 'Essay'),
            ('report', 'Report'),
            ('case_study', 'Case Study'),
            ('presentation', 'Presentation'),
        ]
    )

    
    question_ids = fields.One2many(
        string=u'Questions',
        comodel_name='ghu_custom_mba.assessment_question',
        inverse_name='assessment_id',
    )


class GhuAssessmentQuestion(models.Model):
    _name = 'ghu_custom_mba.assessment_question'
    _rec_name = 'name'
    _description = "Assessment Question"

    name = fields.Char('Name', size=128, required=True)

    question = fields.Text('Question', required=True)

    assessment_id = fields.Many2one(
        string=u'assessment',
        comodel_name='ghu_custom_mba.assessment',
        ondelete='cascade',
    )
    