import type { ProjectUser } from "./ProjectUser"
import type { ProjectCategory } from "./ProjectCategory"

export interface Project{
	name: string
	creation: string
	modified: string
	owner: string
	modified_by: string
	docstatus: 0 | 1 | 2
	parent?: string
	parentfield?: string
	parenttype?: string
	idx?: number
	/**	Series : Select	*/
	naming_series: "PROJ-.####"
	/**	Project Name : Data	*/
	project_name: string
	/**	Status : Select	*/
	status?: "Open" | "Completed" | "Cancelled"
	/**	Project Type : Link - Project Type	*/
	project_type?: string
	/**	Category : Link - Project Category	*/
	category?: string
	category_details?: ProjectCategory
	/**	Is Active : Select	*/
	is_active?: "Yes" | "No"
	/**	% Complete Method : Select	*/
	percent_complete_method?: "Manual" | "Task Completion" | "Task Progress" | "Task Weight"
	/**	% Completed : Percent	*/
	percent_complete?: number
	/**	From Template : Link - Project Template	*/
	project_template?: string
	/**	Expected Start Date : Date	*/
	expected_start_date?: string
	/**	Expected End Date : Date	*/
	expected_end_date?: string
	/**	Priority : Select	*/
	priority?: "Medium" | "Low" | "High"
	/**	Department : Link - Department	*/
	department?: string
	/**	Team : Link - Department	*/
	team?: string
	/**	Customer : Link - Customer	*/
	customer?: string
	/**	Sales Order : Link - Sales Order	*/
	sales_order?: string
	/**	Users : Table - Project User - Project will be accessible on the website to these users	*/
	users?: ProjectUser[]
	/**	Copied From : Data	*/
	copied_from?: string
	/**	Notes : Text Editor	*/
	notes?: string
	/**	Actual Start Date (via Timesheet) : Date	*/
	actual_start_date?: string
	/**	Actual Time in Hours (via Timesheet) : Float	*/
	actual_time?: number
	/**	Actual End Date (via Timesheet) : Date	*/
	actual_end_date?: string
	/**	Estimated Cost : Currency	*/
	estimated_costing?: number
	/**	Total Costing Amount (via Timesheet) : Currency	*/
	total_costing_amount?: number
	/**	Total Purchase Cost (via Purchase Invoice) : Currency	*/
	total_purchase_cost?: number
	/**	Company : Link - Company	*/
	company: string
	/**	Total Sales Amount (via Sales Order) : Currency	*/
	total_sales_amount?: number
	/**	Total Billable Amount (via Timesheet) : Currency	*/
	total_billable_amount?: number
	/**	Total Billed Amount (via Sales Invoice) : Currency	*/
	total_billed_amount?: number
	/**	Total Consumed Material Cost (via Stock Entry) : Currency	*/
	total_consumed_material_cost?: number
	/**	Default Cost Center : Link - Cost Center	*/
	cost_center?: string
	/**	Gross Margin : Currency	*/
	gross_margin?: number
	/**	Gross Margin % : Percent	*/
	per_gross_margin?: number
	/**	Collect Progress : Check	*/
	collect_progress?: 0 | 1
	/**	Holiday List : Link - Holiday List	*/
	holiday_list?: string
	/**	Frequency To Collect Progress : Select	*/
	frequency?: "Hourly" | "Twice Daily" | "Daily" | "Weekly"
	/**	From Time : Time	*/
	from_time?: string
	/**	To Time : Time	*/
	to_time?: string
	/**	First Email : Time	*/
	first_email?: string
	/**	Second Email : Time	*/
	second_email?: string
	/**	Daily Time to send : Time	*/
	daily_time_to_send?: string
	/**	Day to Send : Select	*/
	day_to_send?: "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" | "Saturday" | "Sunday"
	/**	Weekly Time to send : Time	*/
	weekly_time_to_send?: string
	/**	Subject : Data	*/
	subject?: string
	/**	Message : Text - Message will be sent to the users to get their status on the Project	*/
	message?: string

	rd_template?: string;
	/** Tasks completed this week : Number - Count of tasks completed in the current week	*/
	tasks_completed_this_week?: number;
	department_migrated?:string
}


import type { TaskDependsOn } from './TaskDependsOn'

export interface Task{
	name: string
	creation: string
	modified: string
	owner: string
	modified_by: string
	docstatus: 0 | 1 | 2
	parent?: string
	parentfield?: string
	parenttype?: string
	idx?: number
	/**	Subject : Data	*/
	subject: string
	/**	Project : Link - Project	*/
	project?: string
	/**	Issue : Link - Issue	*/
	issue?: string
	/**	Type : Link - Task Type	*/
	type?: string
	/**	Color : Color	*/
	color?: string
	/**	Is Group : Check	*/
	is_group?: 0 | 1
	/**	Is Template : Check	*/
	is_template?: 0 | 1
	/**	Status : Select	*/
	status?: "Open" | "Working" | "Pending Review" | "Overdue" | "Template" | "Completed" | "Cancelled"
	/**	Priority : Select	*/
	priority?: "Low" | "Medium" | "High" | "Urgent"
	/**	Is Important : Check	*/
	is_important?: 0 | 1
	/**	Weight : Float	*/
	task_weight?: number
	/**	Parent Task : Link - Task	*/
	parent_task?: string
	/**	Completed By : Link - User	*/
	completed_by?: string
	/**	Completed On : Date	*/
	completed_on?: string
	/**	Assigned To : Link - Employee	*/
	assigned_to?: string
	/**	Expected Start Date : Date	*/
	exp_start_date?: string
	/**	Expected Time (in hours) : Float	*/
	expected_time?: number
	/**	Begin On (Days) : Int	*/
	start?: number
	/**	Expected End Date : Date	*/
	exp_end_date?: string
	/**	% Progress : Percent	*/
	progress?: number
	/**	Duration (Days) : Int	*/
	duration?: number
	/**	Is Milestone : Check	*/
	is_milestone?: 0 | 1
	/**	Task Description : Text Editor	*/
	description?: string
	/**	Dependent Tasks : Table - Task Depends On	*/
	depends_on?: TaskDependsOn[]
	/**	Depends on Tasks : Code	*/
	depends_on_tasks?: string
	/**	Actual Start Date (via Timesheet) : Date	*/
	act_start_date?: string
	/**	Actual Time in Hours (via Timesheet) : Float	*/
	actual_time?: number
	/**	Actual End Date (via Timesheet) : Date	*/
	act_end_date?: string
	/**	Total Costing Amount (via Timesheet) : Currency	*/
	total_costing_amount?: number
	/**	Total Expense Claim (via Expense Claim) : Currency	*/
	total_expense_claim?: number
	/**	Total Billable Amount (via Timesheet) : Currency	*/
	total_billing_amount?: number
	/**	Review Date : Date	*/
	review_date?: string
	/**	Closing Date : Date	*/
	closing_date?: string
	/**	Department : Link - Department	*/
	department?: string
	/**	Company : Link - Company	*/
	company?: string
	/**	lft : Int	*/
	lft?: number
	/**	rgt : Int	*/
	rgt?: number
	/**	Old Parent : Data	*/
	old_parent?: string
	/**	Template Task : Data	*/
	template_task?: string
}


export interface TaskDependsOn{
	name: string
	creation: string
	modified: string
	owner: string
	modified_by: string
	docstatus: 0 | 1 | 2
	parent?: string
	parentfield?: string
	parenttype?: string
	idx?: number
	/**	Task : Link - Task	*/
	task?: string
	/**	Subject : Text	*/
	subject?: string
	/**	Project : Text	*/
	project?: string
}