
import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.workflow.JiraWorkflow
import com.atlassian.jira.workflow.WorkflowManager
import java.util.regex.Matcher

String searchText = 'workflow'

WorkflowManager workflowManager = ComponentAccessor.getWorkflowManager()
Collection<JiraWorkflow> workflows = workflowManager.getWorkflows()

String result = ""

workflows.each{workflow ->
    String workflow_name = "${workflow.name}${if(workflow.isActive()){"(active)"} }"
    result += "$workflow_name, "
    String workflow_description = "${workflow.description}${if(workflow.isActive()){"(active)"} }"
    result += "$workflow_description,"
    String workflow_actions = "${workflow.allActions}${if(workflow.isActive()){"(active)"} }"
    result += "$workflow_actions;"
}
result
