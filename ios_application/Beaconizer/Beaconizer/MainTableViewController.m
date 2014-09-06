

#import "MainTableViewController.h"

@implementation MainTableViewController

    - (void)viewDidLoad{
        [super viewDidLoad];
        _UrlsToDisplayInTable = [NSArray arrayWithObjects:@"testURL1", @"testURL2", nil];
    }

    - (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
    {
        return [_UrlsToDisplayInTable count];
    }


    - (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
    {
        static NSString *CellIdentifier = @"URLofBeacon";
        
        UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
        
        if (cell == nil) {
            cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
        }
        
        cell.textLabel.text = [_UrlsToDisplayInTable objectAtIndex:indexPath.row];
        
        return cell;
    }

@end
