from crontab import CronTab
import datetime

my_crons = CronTab(user='danielmueller')


# # show name and frequency
# for job in my_crons:
#     print (job)
#     print (job.frequency())
#     print (job.frequency_per_hour())


# ## Adding jobs
# job = my_crons.new(command='python /Users/danielmueller/learningcenter/writeDate.py', comment='dateinfo')
# job.minute.every(1)
# my_crons.write()

## Adding jobs
# job = my_crons.new(command='python /Users/danielmueller/learningcenter/writeDate.py', comment='date')
# job.minute.every(1)
# my_crons.write()

# # show job only, if it has comment
# for job in my_crons:
#     if job.comment == 'dateinfo':
#         print (job, job.comment)


# # reschedule
# for job in my_crons:
#     if job.comment == 'dateinfo':
#         job.minute.every(2)
#         my_crons.write()
#         print ('Cron job modified successfully')

#
# # delete job
# for job in my_crons:
#     if job.comment == 'dateinfo':
#         my_crons.remove(job)
#         my_crons.write()
#         print('Cron job deleted successfully')

for job in my_crons:
    sch = job.schedule(date_from=datetime.datetime.now())
    print (job, sch.get_next())


# Examples:
# https://tecadmin.net/crontab-in-linux-with-20-examples-of-cron-schedule/